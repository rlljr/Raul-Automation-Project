import re

# st = r'\nhello\tthere'
# print(st)
# print(type(st))
######################################################
with open('show_version.txt') as ver_data: #open the show version file
    ver_output = ver_data.read()
#
# my_pattern = r"Cisco" # Regex Pattern
# re_output = re.search(pattern=my_pattern, string=ver_output)#search means just the first occurence
# print(re_output.group(0))
##################################################################

# my_pattern = r"Cisco.+, Version (\d\S+)"
# re_output = re.search(pattern=my_pattern, string=ver_output)
# version_output = re_output.group(1)
#
# print(f"{'IOS Version:'.ljust(18)}: {version_output}")
################################################

# my_pattern = r"(cisco)\.(com)"#\\. escape charter for . group1 is cisco and com is group2
# re_output = re.search(pattern=my_pattern, string=ver_output)
#
# if re_output:
#     print("Match found")
#     print(re_output.group(0))
#     print(re_output.group(1))
#     print(re_output.group(2))
# else:
#     print("Match not found")
#####################################################
# '''compile'''
# my_pattern = re.compile(r"(cisco)\.(\w+)") #\w means any word character, + symbol match til the end
# result = my_pattern.search(string=ver_output)
# print(result)
# print(result.group(0))

#####################################################
'''compile Example'''
# my_pattern = re.compile(r"C....")
# #print(my_pattern.search(string=ver_output))#only finds the first occurence
# #print(my_pattern.findall(string=ver_output))
# results = my_pattern.finditer(string=ver_output)
# for result in results:
#     print(result)
#     print(result.group())
#     print(result.span())#span Method returns a tuple containing starting and ending index of the matched string.
# #####################################################
# '''Validate User input '''
# # python3 or python3.10
# input1 = input("Enter Python Version:").casefold()
# my_pattern = re.compile(r"python3(\.10)?\Z")
# match = my_pattern.search(input1)
# if match:
#     print(f"Matched with {input1}")
# else:
#     print("Not matched")

#####################################################
'''Email validation pattern'''
# support_mail = 'please reach out to help@gmail.com, support@gmail.com, admin@gmail.co.in ab@abc.co.us, abc@aa.co.uk'
# email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+.co[m|\.](\w{2})?")
# results = email_pattern.finditer(support_mail)
# for result in results:
#     print(result.group())


''' 
^ \Z matches only with single line

^ : (Caret.) Matches the start of the string, 
and in MULTILINE mode also matches immediately after each newline.

\Z : Matches the end of the string or just before the newline at the end of the string,
 and in MULTILINE mode also matches before a newline.

\A : Matches only at the start of the string.

\Z : Matches only at the end of the string.

\A and \Z scans entire multiline and prints last result'''
###############################################################
#str1 = """DC01 IND R1"""

str1 = """DC01 IND R1
DC02 US R1
DC03 UK R1"""

# print(re.search(pattern=r"^D.+1$", string=str1))
# print(re.findall(pattern=r"^D.+1$", string=str1))
# r = re.finditer(pattern=r"^D.+1$", string=str1)
# for data in r:
#     print(data.group())
####################################
# print(re.search(pattern=r"^D.+1\Z", string=str1, flags=re.MULTILINE))
# print(re.findall(pattern=r"^D.+\Z", string=str1, flags=re.MULTILINE))
# r = re.finditer(pattern=r"^D.+1\Z", string=str1, flags=re.MULTILINE)
# for data in r:
#     print(data.group())

############################################
'''
\b :Matches the empty string,
 but only at the beginning or end of a word. 

 \B
Matches the empty string, word should be in the middle  
 '''
#matches empty string only at beginning or end
# my_pattern = re.compile(r'\Bcisco')
# string1 = 'ciscoroutercciscowerwer'
# print(my_pattern.search(string1))
############################################
# '''{m,n}'''
# my_pattern = re.compile(r'cisco{2,5}')
# string1 = 'ciscorouterciscoo'
# print(my_pattern.search(string1))
# ############################################
''' \''''
#noinspection PyRedeclaration
my_pattern = re.compile(r'\*\n')
print(my_pattern.search(ver_output))
############################################

'''IGNORECASE'''
# print(re.search('hello', 'Hello', re.I))
############################################
'''DOTALL
by default, dot matches any character except the newline'''

# print(re.search('hello.hello', 'Hello\nHello', flags= re.DOTALL | re.IGNORECASE))
# print(re.search('hello.hello', 'Hello\nHello'))

# ############################################
# '''match'''
# my_string = 'abcd1234abcd'
# # print(re.match('abcd', my_string)) # None
# # print(re.search('1234abcd', my_string)) # match:
# print(re.fullmatch('abcd1234abcd', my_string)) # match
#
# ############################################
# '''sub'''
# # noinspection PyRedeclaration
# my_string = 'VLAN100 ip address 1.1.1.1 VLAN200, VLAN300'
# # print(re.sub(r'V', r'Vx', my_string))
# print(re.subn(r'V', r'Vx', my_string))