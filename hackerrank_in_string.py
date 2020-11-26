import re

def hackerrank_in_string(string):
    result = re.match("^.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k",string)
    if result:
        return "YES"
    else:
        return "NO"


total_queries = int(input())
for _ in range(total_queries):
    string = input()
    print(hackerrank_in_string(string))
