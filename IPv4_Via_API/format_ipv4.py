import binascii
import itertools 
import socket

def upgrade_ip(ip, subnet, lower_range, upper_range):
    ip_temp = ip.split('.')
    first_byte = ip_temp[0]
    second_byte = ip_temp[1]
    third_byte = ip_temp[2]
    fourth_byte = ip_temp[3]
    ip_list = []

    if subnet > lower_range and subnet < upper_range:                               # upgrate subnet.
        difference = subnet - lower_range
        binary = bin(int(second_byte))
        binary = binary[2:len(ip)-2]                                                # remove xb
        if len(binary) < 8:                                                         # make binary len == to 8
            while len(binary) != 8:
                binary = str(0)+binary
          
        n = 8 - difference
        lst = list(itertools.product(['0', '1'], repeat=n))                         # combinations of ip
    
        for index in lst:
            new_sum = index[0]
            for j in range(1, len(index)):
                new_sum += index[j]

            second_byte = str(int((binary[0:difference] + new_sum), 2) )
            single_ip = first_byte+"."+second_byte+"."+third_byte+"."+fourth_byte
            ip_list.append(single_ip)

    return ip_list
        
def split_IP_and_covert_to_Hex(ipv4):
    ipv4 = ipv4.split('/')
    ip = ipv4[0]
    subnet = ipv4[1]
    hex_ip_list = []

    # print(subnet)
    subnet = int(subnet)
    if subnet < 8:
        ip_list = upgrade_ip(ip, subnet, 0, 8)
        subnet = str(8)

    elif subnet > 8 and subnet < 16:                                                  # upgrate subnet.
        ip_list = upgrade_ip(ip, subnet, 8, 16)
        subnet = str(16)

    elif subnet > 16 and subnet < 24:
        ip_list = upgrade_ip(ip, subnet, 16, 24)
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
    files_index+=1 


    
    



