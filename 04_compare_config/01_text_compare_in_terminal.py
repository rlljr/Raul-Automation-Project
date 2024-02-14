import difflib

#open both files
with open('golden_conf.txt') as g_data:#original file
    g_config = g_data.read()#set variable from g_data

with open('new_conf.txt') as n_data:#new file
    n_config = n_data.read()#set variable from n_data

#we'll get both file

delta = difflib.Differ().compare(g_config.splitlines(), n_config.splitlines())#comparison
print(delta)
#output would be a generator
#<generator object Differ.compare at 0x1088a1430>


for data in delta:
    print(data)
