import ssh_function
import re
from  ssh_function import cisco_cmd_executor
hosts = ["172.16.20.154", "172.16.20.210"]
show_run_command = ["show ver | i Base ethernet MAC Address"]
mac_pattern = re.compile(r'Base ethernet MAC Address       : (\S+)')



x=[]
y=[]
for i in range(len(hosts)):
    x.append(cisco_cmd_executor(hosts[i],show_run_command))
    for z in range(len(x)):
        print(i)
        mac_match = mac_pattern.search(x[z])
    y.append(mac_match.group(1))
    #print("ip address " + hosts[i] + "has mac address " + mac_match.group(1))
print(y)


