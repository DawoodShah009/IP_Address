"""
This program collects the IP addresses of a Certain cdn.
Input: Cdn's ASN
Output: IP addresses
Working: 
     For example: for Akamai, write 'python get_data.py $filename' press Enter
                    then enter 12222(Akamai's ASN)
"""
import requests

asn = str(input("\n"))

url = 'https://api.bgpview.io/asn/'+asn+'/prefixes'
r = requests.get(url)

data = r.json()
object_list = data['data']['ipv4_prefixes']
for object in object_list:
     print(object['prefix'])