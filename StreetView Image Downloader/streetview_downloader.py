# required Libraries 
import google_streetview.api
import google_streetview.helpers

lat, lon = 42.0451, -87.6051 # pass in the latitude and longitude of the area you need images for. 
radius = 1                              # how many miles you need the images for. 
increment = 0.2                         # steps it should skip to capture the images.
download_data_dir = "./GSV_images/"     # Save downloaded images to this location. 
api_key = ""                            # Create your own googlestreetview Api from google cloud console

"""
SIZE : 
    Size of the image in pixels, by default is 640X640
HEADING : 
    The camera direction with respect to north.
FOV : 
    Horizontal field of view 
PITCH : 
    Adjust the camera’s up and down angle with the --pitch argument, 
"""
params = {
        'size': '640x640',          
        'heading': '0;90;180;270',  
        'fov': '90;120',   
        'pitch': '0',
        }

def get_images(latitude, longitude, radius, increment, api_key, data_dir, parameters):
    '''
    Fucntion to download the images to the designated location. 

    Params : 
        - latitude, longitude (int, int): GPS cordinates of the location on interest. 
        - radius                   (int): Radius to get images from the location 
        - increment              (float): after how many intervals the imgaes to be clicked. 
        - api_key                  (str): google authorization key from the streetview API 
        - data_dir                 (str): image save location 
        - parameters              (dict): image attributes needed to download. 

    Returns: 
        - images downloaded in the data_dir
    '''
    lat_difference = increment/69
    long_difference = increment/54

    lat_dim = radius/(69*2)
    long_dim = radius/(54*2)

    # making a list of all the latitude and longitude intersections 

    lat_lower = latitude - lat_dim
    long_east = longitude + long_dim

    lat_upper = latitude + lat_dim
    long_west = longitude - long_dim

    cordinates = []

    lat = lat_lower
    lon = long_west

    while lat <=lat_upper:
        while lon <= long_east:
            temp = str(lat) +','+str(lon)+';'
            cordinates.append(temp)
            lon += long_difference
        lat += lat_difference
        lon = long_west

            
    API_locations = ''.join(cordinates)

    apiargs = parameters 

    apiargs['location'] = API_locations
    apiargs['key'] = api_key

    # Get a list of all possible queries from multiple parameters
    api_list = google_streetview.helpers.api_list(apiargs)

    # Create a results object for all possible queries provides metadata 
    # of downloaded images
    results = google_streetview.api.results(api_list)

    print("downloading starting")

    #Download images to directory 'downloads'
    results.download_links(data_dir)

    print("downloading done !")