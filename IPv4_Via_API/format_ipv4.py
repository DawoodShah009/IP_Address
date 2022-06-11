import binascii
from hashlib import new
import itertools 
import socket
def upgrade_ip(ip, subnet, lower_range, upper_range, byte_to_change, bits_to_change, ip_list):
    ip_temp = ip.split('.')
    byte = ip_temp[byte_to_change]

    if subnet > lower_range and subnet < upper_range:                               
        difference = subnet - lower_range
        binary = bin(int(byte))

        binary = binary[2:len(ip)]   
        
        if len(binary) < 8:                                                         
            while len(binary) != 8:
                binary = str(0)+binary

        network_portion = binary[0:(8-bits_to_change)]

        n = 8 - difference
        lst = list(itertools.product(['0', '1'], repeat=n))   
        for index in lst[1:]:
            
            value = ''.join(index)
            new_byte = int(network_portion+value,2)
            ip_temp[byte_to_change] = str(new_byte)
            ip_address = '.'.join(ip_temp)
            ip_list.append(ip_address)

    return ip_list
        
def split_IP_and_covert_to_Hex(ipv4, ip_list):

    ipv4 = ipv4.split('/')
    ip = ipv4[0]
    ret_ip = ip
    subnet = ipv4[1]
    subnet = int(subnet)
    
    if subnet < 8:
        bits_to_change = 8-subnet
        ip_list = upgrade_ip(ip, subnet, 0, 8, 0, bits_to_change, ip_list)
        
    elif subnet > 8 and subnet < 16:   # upgrate subnet.
        bits_to_change = 16-subnet
        ip_list = upgrade_ip(ip, subnet, 8, 16, 1, bits_to_change, ip_list)

    elif subnet > 16 and subnet < 24:
        bits_to_change = 24-subnet
        ip_list = upgrade_ip(ip, subnet, 16, 24, 2, bits_to_change, ip_list)            #104.101.220.0/23

    subnet = str(subnet)
    ip = str(binascii.hexlify(socket.inet_aton(ret_ip)).upper())
    ip = ip[2:len(ip)-2]
    hex_ip = "0x"+ip
    return hex_ip , ip_list, subnet, ret_ip
        
    

list_of_files = ["akamai","amazon_cloudfront","aryaka","cachefly","cdn77","cdnetworks","cloudfare","fastly",
                 "incapsula","limelight01","limelight02","rackspace01","rackspace02","softlayer","stackpath"]
val_list = [8,16,24]
length = len(list_of_files)
files_index = 0
check_list = []    
while files_index < length:
    ip_list = []
    final_list = []
    file = list_of_files[files_index]
    ip_file = open(file+".txt", "r")
    var = file.upper()
    if files_index == (length-1):
        print("/*CDN_"+var+"*/")
    else:
        print("/*APPLICATION_"+var+"*/")
        
    
    for index, ipv4  in enumerate(ip_file):   
  
        hex_ip , ip_list, subnet, ip = split_IP_and_covert_to_Hex(ipv4, ip_list)
        if (ip not in final_list) and (ip not in ip_list):
            print(" ","{",hex_ip,"/*",ip,"*/,",subnet+",",var,"},") 
            final_list.append(ip)
                  
    files_index+=1 
