# [ Name ]:             OVHcloud VPS auto-rebuild
# [ Version ]:          1.0
# [ Author ]:           Christian Goeschel Ndjomouo
# [ Created on ]:       Sep 25 2023
# [ Last updated on ]:  Sep 26 2023
# [ Tested on ]:        Python v3.9
#
# [ Description ]:      This program automates the rebuild of your OVHcloud VPS
#                       The app parameters are imported from ovh_app_params.py

# Import needed modules
import ovh
import json
import sys
from ovh_app_params import client_params

client = ovh.Client(
    endpoint= client_params['endpoint'],
    application_key= client_params['application_key'],
    application_secret= client_params['application_secret'],
    consumer_key= client_params['consumer_key'],
)

# VPS to reinstall
vps_name = ""

# Function that will query all available images for the specified VPS
def available_images(vps_name):

    global image_id_list

    # Set path variable to API PATH for available OS images [  /vps/{serviceName}/images/available  ]
    path = str(f"/vps/{vps_name}/images/available")

    print(f"\n[ Retrieving available OS images for {vps_name} ... ]\n\n")

    # Print nice welcome message
    image_id_list = json.dumps( client.get(path) , indent=4 ).split('"')

    for i in range(0,len(image_id_list)-1):

        try:
            if '\n' in image_id_list[i]:
                del image_id_list[i]
            else:
                continue
        except:
            break

    return image_id_list

# Function that will map the retrieved available images ids to their queried names via an API call loop
def map_image_ids(image_id_list):

    global image_name_map

    image_name_index = 0                                                            # Index value of the image name in the retrieved JSON data
    image_name_map = {}                                                             # Image ID to Name map

    path = str(f"/vps/{vps_name}/images/available/")                                # API path ( /vps/{serviceName}/images/available/{id} )
    counter = 0                                                                     # Iteration counter

    print(f"[ Executing API call to {path} with all image IDs ]\n\n")

    for id in image_id_list:                                                        # 'id' is an iterated item from the image_id_list

        counter += 1
        image_name_get = json.dumps( client.get(path+id) ).split('"')               # Queries the image name of the selected image id (id) from the API
        image_name_map[ image_name_get[ image_name_get.index('name') + 2 ] ] = id   # Takes the queried name and creates a new dictionary key with 'id' as value
        
        # Progress bar 
        progress_bar =  str("=" * counter) + str(" " * (len(image_id_list) - counter))
        message = str(f"[{progress_bar}] | Updating cache: " + str(counter) + f" | Progress {round((counter / len(image_id_list)) * 100, 2)} %")
        sys.stdout.write("\r" + message)   
        sys.stdout.flush()
      
    # Write image name-id mapping to image_map.json  
    with open("image_map.json", "w") as image_map_file:
        json.dump(image_name_map , image_map_file) 
    
    print("\n\n")


# Function that loads the image_map.json and creates a image name:id dictionary
def image_map_json_decode():

    global image_name_map

    # Opening image_map.json file
    json_file = open("image_map.json", "r")

    # Converting JSON Data to a Python <dict> object
    image_name_map = json.load(json_file)

    # Closing the image_map.json file
    json_file.close()

    return image_name_map


# Function that will print all available image names in respective order
def list_images(image_name_map):

    global image_name_list
    image_name_list = list(image_name_map.keys())   # Creates a list from the keys in image_name_map in respective order
    counter = 1

    print(f"[ Available images for {vps_name} are: ] \n\n")

    for image_name in image_name_list:

        print(f"[ {counter} ] {image_name}\n")
        counter += 1


# Function that will request user input to determine the reinstallation image 
def user_input():

    print("\n[ Image Selection ]\n")
    print("Which image would you like to install ?", end=" ")
    image_selection = int(input("Type in a number from above: "))

    if image_selection > len(image_name_list) or image_selection < 1:
        print(f"\n[ INVALID INPUT ] Aborting ...")
        sys.exit()
    else:
        return image_selection


# Function that will perform the VPS reinstall API call
def reinstall(vps_name, image_selection):

    image_selection_id = image_name_map[ image_name_list[image_selection-1] ]     # Getting image selection ID
    print(image_selection)

    # Set API PATH for VPS reinstallation [  /vps/{serviceName}/rebuild ]
    path = str(f"/vps/{vps_name}/rebuild")

    # Information output
    print(f"\n[ Executing VPS reinstall for {vps_name} with {image_name_list[image_selection-1]} ... ]\n\n")

    # Sending VPS reinstall API call 
    reinstall_call_result = json.dumps( client.post(path, doNotSendPassword=False, imageId=image_selection_id, installRTM=False, sshKey=None, ) , indent=4 )

    # Printing API call result
    print(reinstall_call_result)



# Function that determines the flow of the program
# User can decide whether to refresh / initialize the image list cache or to use the existing one
# The ladder will cut down the processing time by 80% 
def functions_call():

    user_choice = input("Do you want to refresh/initialize the image list cache ? ( Y / N ): ")
    
    if user_choice.lower() == "y":

        map_image_ids( available_images(vps_name) )     # If user wants to refresh cache
        list_images(image_name_map)
        reinstall(vps_name, user_input() )

    elif user_choice.lower() == "n":  
                           
        list_images( image_map_json_decode() )
        reinstall(vps_name, user_input() )
    
    else:
        print(f"\n[ INVALID INPUT ] Aborting ...")
        sys.exit()

# Starting program
functions_call()


    


    
