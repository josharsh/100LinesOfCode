import subprocess, os
import boto3
from datetime import datetime
from botocore.exceptions import ClientError
from configparser import ConfigParser, NoOptionError, NoSectionError
from boto3_type_annotations.s3 import Client

class ConfigError(Exception):
    def __init__(self, message):
        self.message = message


class BackupCreationError(Exception):
    def __init__(self, message):
        self.message = message


def current_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))

class Config:
    def __init__(self, filename: str = "secrets.conf"):
        conf = ConfigParser()
        conf.read(os.path.join(current_path(), filename))
        self.conf = conf

    def get_conf(self) -> ConfigParser:
        return self.conf

    def get(self, section: str, option: str):
        if section is None or option is None:
            raise ConfigError("Please provide both SECTION and OPTION")
        try:
            return self.conf.get(section, option)
        except NoOptionError as e:
            raise ConfigError(f"There is no option {option} in section {section}")
        except NoSectionError as e:
            raise ConfigError(
                f"There is no section {section} in the configuration provided"
            )
        except Exception as e:
            raise ConfigError(f"An unknown error occured. {e}")

def create_backup(config: Config) -> str:
    today = datetime.now()
    timestamp = today.strftime("%Y-%m-%d")
    filename_base = config.get("backup_data", "filename")
    filename = f"{filename_base}-{timestamp}.tar.gz"
    # script = f"tar czf {filename} env"
    volume_name = config.get("backup_data", "volume_name")
    volume_directory = config.get("backup_data", "volume_directory")
    path_name = current_path()
    script = f"docker run --rm --volume {volume_name}:{volume_directory} --volume {path_name}:/backup   ubuntu   tar czf /backup/{filename} {volume_directory}"
    process = subprocess.run(
        script.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE
    )
    if process.returncode != 0:
        raise BackupCreationError(
            f"Backup could not be created.\n{process.stderr.decode('utf-8')}"
        )
    return filename

def upload_file(file_name: str, bucket_name: str, s3_client: Client) -> bool:
    today = datetime.now()
    try:
        response = s3_client.upload_file(os.path.join(current_path(), file_name), bucket_name, file_name)
    except ClientError as e:
        print(e)
        return False
    return True

def get_s3_client(conf: Config) -> Client:
    return boto3.client(
        "s3",
        aws_access_key_id=conf.get("aws_s3_credentials", "access_key_id"),
        aws_secret_access_key=conf.get("aws_s3_credentials", "secret_key"),
    )

def run():
    conf = Config()
    backup_filename = create_backup(conf)
    upload_success = upload_file(
        file_name=backup_filename,
        bucket_name=conf.get("aws_s3_bucket", "name"),
        s3_client=get_s3_client(conf),
    )
    if upload_success:
        subprocess.run(f"rm {os.path.join(current_path(), backup_filename)}".split())

if __name__ == "__main__":
    run()
    print("Done!")

