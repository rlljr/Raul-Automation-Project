import sys
import time
import traceback
from paramiko import client, ssh_exception
from getpass import getpass
import socket
import datetime
#
# with open('show_commands.txt', 'r') as conf_file:
#     new_cmd = conf_file.readlines()
# print(new_cmd)
#
# def cisco_cmd_executor(hostname, commands, username, password):
#     try:
#         print(f"Connecting to the device {hostname}..")
#         now = datetime.datetime.now().replace(microsecond=0)
#         current_conf_file = f"{now}_{hostname}.txt"
#         ssh_client = client.SSHClient()
#         ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
#         ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
#                            allow_agent=False)
#
#         print(f"Connected to the device {hostname}")
#         device_access = ssh_client.invoke_shell()
#         device_access.send("terminal len 0\n")
#
#         for cmd in enumerate(commands, start=1):
#             file_name = f"{str(now).replace(' ', ':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ', '_').strip()}.txt"
#             with open(file_name, 'w') as cmd_data:
#                 device_access.send(f"{cmd[1]}")
#                 time.sleep(1)
#                 output = device_access.recv(65535)
#                 cmd_data.write(output.decode())
#                 print(output.decode(), end='')
#
#     except ssh_exception.NoValidConnectionsError:
#         print("SSH Port not reachable")
#     except socket.gaierror:
#         print("Check the hostname")
#     except ssh_exception.AuthenticationException:
#         print("Authentication failed, check credentials")
#
#     except:
#         print("Exception Occurred")
#         print(sys.exc_info())
#         # traceback.print_exception(*sys.exc_info())
#
# cisco_cmd_executor('csr1.test.lab', new_cmd, 'admin', 'admin')


username = 'admin'
password = 'cisco!123'
csr_cmd = ['show run']
with open('show_commands.txt', 'r') as conf_file:
    new_cmd = conf_file.readlines() #store the variable in new_cmd
print(new_cmd)

def cisco_cmd_executor(hostname, commands):
    try:
        print(f"Connecting to the device {hostname}..")
        now = datetime.datetime.now().replace(microsecond=0)
        current_conf_file = f"{now}_{hostname}.txt"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                           allow_agent=False)

        print(f"Connected to the device {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        #with open(current_conf_file, 'w') as cmd_data: #we can remove this logic
        #the file creation would now be within the for loop
        for cmd in enumerate(commands, start = 1):
            file_name = f"{str(now).replace(' ', ':')}_{cmd[0]}_{cmd[1].strip().replace(' ', '')}.txt"
            with open(file_name, 'w') as cmd_data:
                device_access.send(f"{cmd[1]}\n")#we removed the \n here. If we don't it press enter
                time.sleep(1)
                output = device_access.recv(65535)
                cmd_data.write(output.decode())
                print(output.decode(), end='')

    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check credentials")

    except:
        print("Exception Occurred")
        print(sys.exc_info())
        # traceback.print_exception(*sys.exc_info())

cisco_cmd_executor('172.16.20.154', new_cmd) #we need to pass the list to the csr_cmd function
