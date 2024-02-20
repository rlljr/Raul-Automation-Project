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

def cisco_cmd_executor(hostname, commands):
    print(f"Connecting to the device {hostname}..")
    try:
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")

        for cmd in commands:
            command_output =""
            device_access.send(f"{cmd}\n")
            time.sleep(1)
            output = device_access.recv(65535)
            #print(output.decode(), end='')
            command_output +=output.decode()
        ssh_client.close()
        return command_output
    except:
        print('exception occured')
        print(sys.exc_info())
        traceback.print_exception(*sys.exc_info())
        return "False"

