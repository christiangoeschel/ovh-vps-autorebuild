<img src="https://github.com/christiangoeschel/ovh-vps-autorebuild/blob/main/ovhvpsautorebuild.png" width="100%" height="auto"/>

# OVHcloud VPS Auto-rebuild
This Python program will automate the rebuild / reinstall of your OVHcloud VPS in a matter of seconds.

# Installation

The very first step is the installation of OVH's official Python wrapper which works with Python 3.6+

The easiest way to get the latest stable release is to grab it from pypi using pip.

``` Bash
pip install ovh
```

Alternatively, you may get latest development version directly from Git.

``` Bash
pip install -e git+https://github.com/ovh/python-ovh.git#egg=ovh
```

Once this is done you can clone this repo and start setting up the program files.

# Params.json file setup

The ```params.json``` file stores all the API keys that you will have to generate from your OVHcloud account in order to 
allow access to the OVH API from your application.

You can create the keys here: 

<a href="https://eu.api.ovh.com/createApp/">OVH Europe</a><br>
<a href="https://api.us.ovhcloud.com/createApp/">OVH US</a><br>
<a href="https://ca.api.ovh.com/createApp/">OVH North-America</a><br>
<a href="https://eu.api.soyoustart.com/createApp/">So you Start Europe</a><br>
<a href="https://ca.api.soyoustart.com/createApp/">So you Start North America</a><br>
<a href="https://eu.api.kimsufi.com/createApp/">Kimsufi Europe</a><br>
<a href="https://ca.api.kimsufi.com/createApp/">Kimsufi North America</a><br>
<br>

You will create three keys ```application key```, ```application secret``` and ```consumer secret```. Add these to the params.json file next to the same name JSON key.

Depending on the API you want to use, you may set the ```endpoint``` to:

```ovh-eu``` for OVH Europe API <br>
```ovh-us``` for OVH US API <br>
```ovh-ca``` for OVH North-America API <br>
```soyoustart-eu``` for So you Start Europe API <br>
```soyoustart-ca``` for So you Start North America API <br>
```kimsufi-eu``` for Kimsufi Europe API <br>
```kimsufi-ca``` for Kimsufi North America API <br>

``` Bash
[...]
    "endpoint": " ",
    "application_key": " ",  
    "application_secret": " ",
    "consumer_key": " "
}
```

Save the file and open the rebuild-vps.py file

# Rebuild-vps.py file setup

This file is the main code of the program, it is responsible for the client object creation, API calls, JSON data processing, formatting, visualization and cache file updates.
<br>
The only thing that needs to be edited here is the ```vps_name``` variable that will be your VPS' service name ( vps-xxxxxxxx.vps.ovh.xx ).

``` Python

# Target VPS service name
vps_name = "vps-xxxxxxxx.vps.ovh.xx" 

```

Save the file and run the program with the following command:

```Shell

python rebuild-vps.py

```
<br>
Feel free to read the following guide if you want to know more about the OVH API:
<br>
<a href="https://help.ovhcloud.com/csm/en-ca-api-getting-started-ovhcloud-api?id=kb_article_view&sysparm_article=KB0029722"> First steps with OVH API</a>

Thank you for your support and if you find any bugs please contact me on my LinkedIn or here.

