# [ Name ]:             OVHcloud API client parameter handler
# [ Version ]:          1.0
# [ Author ]:           Christian Goeschel Ndjomouo
# [ Created on ]:       Sep 25 2023
# [ Last updated on ]:  Sep 26 2023
# [ Tested on ]:        Python v3.9
#
# [ Description ]:      This program reads your preset params.json file and pulls out the AK, AS and CK which are used 
#                       to create a Client object to authenticate/sign your OVH API calls in the rebuild-vps.py 


# Importing JSON module
import json

# Parameter dictionary
client_params = {'endpoint':'', 'application_key':'', 'application_secret':'', 'consumer_key':''}

# Pulling all credentials from creds_file and storing them in variables
for i in client_params:

    # Loading creds.json file
    creds_file = open("params.json", "r")

    # Populating the client_params{} with all the attributes parsed from creds.json
    client_params[i] = json.load(creds_file)[i]

    # Closing the creds.json file
    creds_file.close()

