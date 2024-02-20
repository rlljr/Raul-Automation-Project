
import sys
import time
import traceback

from paramiko import client
from getpass import getpass

username = input("Enter Username:")


if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"Enter Password of the user {username}: ") or "admin"

def cisco_cmd_executor(hostname):
    print(f"Connecting to the device {hostname}..")
    try:
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False, timeout=10)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send(" terminal len 0\n")
        device_access.send(f" conf t\n")
        for i in range(15, 40):
            #print("conf t")
            output = "\n"
            time.sleep(1)
            device_access.send(f"int vlan{i}\n")
            time.sleep(1)
            output = device_access.recv(65535)
            print(output.decode(),end='')
            device_access.send(f" ip address 10.10.{i}.{i} 255.255.255.0\n")
            time.sleep(1)
            output = device_access.recv(65535)
            print(output.decode(), end='')
            time.sleep(1)
            if i % 2 == 0:
                time.sleep(1)
                device_access.send(f" description this vlan is even number\n")
                output = device_access.recv(65535)
                print(output.decode(),end="")
            else:
                time.sleep(1)
                device_access.send(f" description this vlan is odd number\n")
                output = device_access.recv(65535)
                print(output.decode(), end="")
            command_output = output.decode()
            #print(command_output)

        ssh_client.close()
    except:
        print('exception occured')
        print(sys.exc_info())
        traceback.print_exception(*sys.exc_info())
        return "False"

cisco_cmd_executor("172.16.20.154")
cisco_cmd_executor("172.16.20.210")

# for i in range(1,101):
#     print("conf t")
#     print(f"loopback interface is : loop{i}")
#     print(f" ip address 10.10.{i}.{i} 255.255.255.255")
