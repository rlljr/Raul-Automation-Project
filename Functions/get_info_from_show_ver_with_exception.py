import ssh_function
import re
import csv
from  ssh_function_with_exception import cisco_cmd_executor
import pandas as pd

hosts = ["172.16.20.154", "172.16.20.211","172.16.20.210", "192.16.10.1"]
show_run_command = ["show ver"]
mac_pattern = re.compile(r'Base ethernet MAC Address       : (\S+)')
model_pattern = re.compile(r'Model number                    : (\S+)')
serial_pattern = re.compile(r'System serial number            : (\S+)')
x=[]
macs=[]
models =[]
complete_list=[]
serials =[]

for i in range(len(hosts)):
    x.append(cisco_cmd_executor(hosts[i],show_run_command))#shows output of the command
    for z in range(len(x)):
        mac_match = mac_pattern.search(x[z])
        model_match = model_pattern.search(x[z])
        serial_match = serial_pattern.search(x[z])
    if mac_match == None:
        macs.append("")
    else:
        macs.append(mac_match.group(1))
    if model_match == None:
        models.append("")
    else:
        models.append(model_match.group(1))
    if serial_match == None:
        serials.append("")
    else:
        serials.append(serial_match.group(1))

complete_list.append(hosts)
complete_list.append(macs)

dict = {'IP address' : hosts, "Mac Addresses" : macs, "Model" : models, "Serial Number" : serials}
df =pd.DataFrame(dict)
df.to_csv('device_list.csv')
print(dict)




