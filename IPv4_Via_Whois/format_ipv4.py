import binascii
import socket
def split_IP_and_covert_to_Hex(ipv4):
    ipv4 = ipv4.split('/')
    ip = ipv4[0]
    subnet = ipv4[1]
    ip = str(binascii.hexlify(socket.inet_aton(ip)).upper())
    ip = ip[2:len(ip)-2]
    hex_ip = "0x"+ip
    return hex_ip,subnet

list_of_files = ["akamai","amazon_cloudfront","aryaka","cachefly","cdn77","cdnetworks","cloudfare","fastly",
                 "incapsula","limelight01","limelight02","rackspace01","rackspace02","softlayer","stackpath"]

length = len(list_of_files)
files_index = 0
while files_index < length:
    file = list_of_files[files_index]
    ip_file = open(file+".txt", "r")
    var = file.upper()
    
    print("/*"+var+"*/")
    
    for index, ipv4  in enumerate(ip_file):
        
        hex_ip,subnet = split_IP_and_covert_to_Hex(ipv4)
        ipv4 = ipv4[ :(len(ipv4)-1)]
        subnet = subnet[ :(len(subnet)-1)]
        print(" ","{",hex_ip,"/*",ipv4,"*/,",subnet+",",var,"},")       
    files_index+=1
    



