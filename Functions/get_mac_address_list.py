import ssh_function
import re
import csv
from  ssh_function import cisco_cmd_executor
import pandas as pd

hosts = ["172.16.20.154", "172.16.20.210"]
show_run_command = ["show ver | i Base ethernet MAC Address"]
mac_pattern = re.compile(r'Base ethernet MAC Address       : (\S+)')
x=[]
macs=[]
my_dict = {}
complete_list=[]

for i in range(len(hosts)):
    x.append(cisco_cmd_executor(hosts[i],show_run_command))
    for z in range(len(x)):
        mac_match = mac_pattern.search(x[z])
    macs.append(mac_match.group(1))
complete_list.append(hosts)
complete_list.append(macs)

dict = {'IP address' : hosts, "Mac Addresses" : macs}
df =pd.DataFrame(dict)
df.to_csv('mac_list.csv')




