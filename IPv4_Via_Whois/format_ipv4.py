import binascii
from hashlib import new
import itertools 
import socket

def upgrade_ip(ip, subnet, lower_range, upper_range, byte_to_change, bits_to_change):
    ip_temp = ip.split('.')
    byte = ip_temp[byte_to_change]
    ip_list = []                    #104.101.220.0/23    16    24   23

    if subnet > lower_range and subnet < upper_range:                               # upgrate subnet.
        difference = subnet - lower_range
        binary = bin(int(byte))
        # print(binary)
        binary = binary[2:len(ip)]   # remove xb
        # binary = binary[2:len(byte)]   # remove xb
        
        # print(binary)
        if len(binary) < 8:                                                         # make binary len == to 8
            while len(binary) != 8:
                binary = str(0)+binary
        # print(binary)
        network_portion = binary[0:(8-bits_to_change)]
        # print(network_portion)
        n = 8 - difference
        lst = list(itertools.product(['0', '1'], repeat=n))      # combinations of ip
    
        for index in lst:

            value = ''.join(index)
            # print("Binary", network_portion+value)
            new_byte = int(network_portion+value,2)
            # print(new_byte)
            ip_temp[byte_to_change] = str(new_byte)
            ip_address = '.'.join(ip_temp)
            ip_list.append(ip_address)

    return ip_list
        
def split_IP_and_covert_to_Hex(ipv4):
    ipv4 = ipv4.split('/')
    ip = ipv4[0]
    subnet = ipv4[1]
    hex_ip_list = []
    subnet = int(subnet)
    
    if subnet < 8:
        bits_to_change = 8-subnet
        ip_list = upgrade_ip(ip, subnet, 0, 8, 0, bits_to_change)
        subnet = str(8)

    elif subnet > 8 and subnet < 16:   # upgrate subnet.
        bits_to_change = 16-subnet
        
        ip_list = upgrade_ip(ip, subnet, 8, 16, 1, bits_to_change)
        subnet = str(16)

    elif subnet > 16 and subnet < 24:
        bits_to_change = 24-subnet
        
        ip_list = upgrade_ip(ip, subnet, 16, 24, 2, bits_to_change)            #104.101.220.0/23
        subnet = str(24)

    elif subnet ==8 or subnet == 16 or subnet >= 24:
        ip_list = [ip]

    subnet = str(subnet)
    for ip in ip_list:
        ip = str(binascii.hexlify(socket.inet_aton(ip)).upper())
        ip = ip[2:len(ip)-2]
        hex_ip = "0x"+ip
        hex_ip_list.append(hex_ip)
    
    return hex_ip_list , ip_list, subnet

list_of_files = ["akamai","amazon_cloudfront","aryaka","cachefly","cdn77","cdnetworks","cloudfare","fastly",
                 "incapsula","limelight01","limelight02","rackspace01","rackspace02","softlayer","stackpath"]
# list_of_files = ["limelight02"]

length = len(list_of_files)
files_index = 0
while files_index < length:
    file = list_of_files[files_index]
    ip_file = open(file+".txt", "r")
    var = file.upper()
    print("/*"+var+"*/")
    
    for index, ipv4  in enumerate(ip_file):       
        hex_ip_list , ipv4_list, subnet = split_IP_and_covert_to_Hex(ipv4)

        for i in range(len(hex_ip_list)):           
            print(" ","{",hex_ip_list[i],"/*",ipv4_list[i],"*/,",subnet+",",var,"},")       
            # pass
    files_index+=1 


    
    



