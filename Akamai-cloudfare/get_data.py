# import requests
import json
# akamai_url = 'https://ipinfo.io/products/asn-api?AS12222'

# r = requests.get(akamai_url)
# data = r.json()
# # print(response.data)
# print(data)
# "https://ipinfo.io/AS12222/json?token=$TOKEN"

########## Akamai ##############
with open('akamai_data.json', 'r') as j:        # reading Akamai JSON file.
     akamai_json = json.loads(j.read())

ipv4 = akamai_json['asn']['prefixes']           # storing the prefixes portion in a list.
akamai_ipv4_list = []
for i in ipv4:
    akamai_ipv4_list.append(i['netblock'])      # storing ipv4 addresses in a list.



########### CloudFare #################
with open('cloudfare_data.json', 'r') as j:     # reading Cloudfare JSON file.
     cloudfare_json = json.loads(j.read())

ipv4 = cloudfare_json['asn']['prefixes']        # storing the prefixes portion in a list.
cloudfare_ipv4_list = []
for i in ipv4:
    cloudfare_ipv4_list.append(i['netblock'])   # storing ipv4 addresses in a list.

