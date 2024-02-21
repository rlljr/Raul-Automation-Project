
from datetime import datetime
import sys
import time
my_string = '''show cdp neighbors detail | i Device ID|Interface
Device ID: raul-terminal-server.raul
Interface: GigabitEthernet1/0/2,  Port ID (outgoing port): GigabitEthernet0/0
Device ID: raul-2960x1.raul
Interface: GigabitEthernet1/0/28,  Port ID (outgoing port): GigabitEthernet1/0/33
Device ID: raul-2960x1.raul
Interface: GigabitEthernet1/0/4,  Port ID (outgoing port): FastEthernet0'''

x = my_string.split("\n")
x=x[1:]
#print(x)
count=0
new_list = [x[i:i + 2] for i in range(0, len(x), 2)]
# print(new_list)
# for i in new_list:
#      for k in i:
#          print(k)
for i in new_list[0]:
    print(i)
#print(y[1])
new_list = []
# print(type(x))


print(datetime.now())
# try:
#     print(out)# res = []
#     for i in range(len(x)):
#
# except:
#     exit()
#     try:
#         res.append(f'{x[idx]} \n {x[idx+1]}')
#     except:
#         continue

# print(res)






