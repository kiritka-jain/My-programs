import re

string_len = int(input())
string = input()
result = re.findall("010",string)
print(len(result))

