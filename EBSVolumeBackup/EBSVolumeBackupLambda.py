import boto3
import collections
import datetime
import time
import sys
today = datetime.date.today()
today_string = today.strftime('%Y/%m/%d')
delete_after_days = 2  # Delete snapshots after this many days
# Except after Monday (at Tuesday ~1am), since Friday is only 2 'working' days away:
if datetime.date.today().weekday() == 1:
    delete_after_days = delete_after_days + 2
deletion_date = today - datetime.timedelta(days=delete_after_days)
deletion_date_string = deletion_date.strftime('%Y/%m/%d')
ec2 = boto3.client('ec2')
regions = ec2.describe_regions().get('Regions', [])
all_regions = [region['RegionName'] for region in regions]


def lambda_handler(event, context):
    snapshot_counter = 0
    snap_size_counter = 0
    deletion_counter = 0
    deleted_size_counter = 0
    for region_name in all_regions:
        print('Instances in EC2 Region {0}:'.format(region_name))
        ec2 = boto3.resource('ec2', region_name=region_name)
        # We only want to look through instances with the following tag key value pair: backup : true
        instances = ec2.instances.filter(
            Filters=[{'Name': 'tag:backup', 'Values': ['true']}])
        volume_ids = []
        for i in instances.all():

            for tag in i.tags:  # Get the name of the instance
                if tag['Key'] == 'Name':
                    name = tag['Value']

            print('Found tagged instance \'{1}\', id: {0}, state: {2}'.format(
                i.id, name, i.state['Name']))

            vols = i.volumes.all()  # Iterate through each instance's volumes
            for v in vols:
                volumeid = ec2.Volume(id=v.id)
                volname = ""
                for tag in volumeid.tags:
                    if tag['Key'] == 'Name':
                        volname = tag.get('Value')
                print(
                    '{0} is attached to volume {1}, proceeding to snapshot'.format(name, v.id))
                volume_ids.extend(v.id)
                snapshot = v.create_snapshot(
                    Description='AutoSnapshot of {0}, on volume {1} - Created {2}'.format(
                        name, v.id, today_string),
                )
                snapshot.create_tags(Tags=[{'Key': 'auto_snap', 'Value': 'true'}, {'Key': 'volume', 'Value': v.id}, {
                                     'Key': 'CreatedOn', 'Value': today_string}, {'Key': 'Name', 'Value': f"{name} autosnap {volname}"}])
                snapshot_counter += 1
                snap_size_counter += snapshot.volume_size
                # Now iterate through snapshots which were made by autsnap
                snapshots = ec2.snapshots.filter(
                    Filters=[{'Name': 'tag:auto_snap', 'Values': ['true']}])
                print(
                    'Checking for out of date snapshots for instance {0}...'.format(name))
                for snap in snapshots:
                    can_delete = False
                    for tag in snap.tags:  # Use these if statements to get each snapshot's
                        # cleated on date, name and auto_snap tag
                        if tag['Key'] == 'CreatedOn':
                            created_on_string = tag['Value']
                        if tag['Key'] == 'auto_snap':
                            if tag['Value'] == 'true':
                                can_delete = True
                        if tag['Key'] == 'Name':
                            snapname = tag['Value']
                    created_on = datetime.datetime.strptime(
                        created_on_string, '%Y/%m/%d').date()

                    if created_on <= deletion_date and can_delete == True:
                        print('Snapshot id {0}, ({1}) from {2} is {3} or more days old... deleting'.format(
                            snap.id, snapname, created_on_string, delete_after_days))
                        deleted_size_counter += snap.volume_size
                        snap.delete()
                        deletion_counter += 1
    print('Made {0} snapshots totalling {1} GB. Deleted {2} snapshots totalling {3} GB'.format(
        snapshot_counter, snap_size_counter, deletion_counter, deleted_size_counter))
    return
