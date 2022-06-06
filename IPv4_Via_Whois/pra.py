# # import itertools
# # lst = list(itertools.product(['0', '1'], repeat=1))      # combinations of ip
# # print(lst)
# # list_ip = []
# # old_ip = '010010'
# # for i in lst:
# #     val = ''.join(i)
# #     new_ip = old_ip+val
# #     list_ip.append(new_ip)
# #     # print(new_ip)
    
    
# # ip = ['1','2','3','4']
# # byte_to_alter = 2
# # for i in list_ip:
# #     ip[2] = i
# #     ans = '.'.join(ip)
# #     print(ans)

# byte = '00110000'
# subnet = 6
# bit_change = 8-subnet
# end = len(byte) - (bit_change)
# byte = byte[0: end]
# print(byte)

print(int('11011100',2))