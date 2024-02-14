# import datetime
#
# with open('show_commands.txt') as sh_cmd:
#     commands = sh_cmd.readlines()
# # time_seq_no_commands
# # print(commands)
# now = datetime.datetime.now().replace(microsecond=0)
# for cmd in enumerate(commands, start=1):
#     file_name = f"{str(now).replace(' ',':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ','_').strip()}.txt"
#     with open(file_name, 'w') as cmd_data:
#         cmd_data.write('test_data')

import datetime
with open('show_commands.txt') as sh_cmd:
    commands = sh_cmd.readlines()
##time_seq_no_commands

# print(commands)
now = datetime.datetime.now().replace(microsecond=0)
for cmd in enumerate(commands, start = 1):#enumerate will create a tuple, without the start=1, the tuple will start with 0
    file_name = f"{str(now).replace(' ', ':')}_{cmd[0]}_{cmd[1].strip().replace(' ','')}.txt"
    with open(file_name, 'w') as cmd_data:
        cmd_data.write('test_data')


