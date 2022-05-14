import json
from traceback import print_tb
import requests

asn = str(input("Enter the asn:\n"))
url = 'https://api.bgpview.io/asn/'+asn+'/prefixes'
r = requests.get(url)

data = r.json()
object_list = data['data']['ipv4_prefixes']
for object in object_list:
     print(object['prefix'])