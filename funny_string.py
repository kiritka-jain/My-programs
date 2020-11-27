def funny_strings(string):
    string_len = len(string)
    diff_list = []
    for index in range(string_len-1):
        difference = abs(ord(string[index+1])-ord(string[index]))
        diff_list.append(difference)
    new_list = list(reversed(diff_list))
    if new_list == diff_list:
        return "Funny"
    else:
        return "Not Funny"


total_queries = int(input())
for _ in range(total_queries):
    string = input()
    print(funny_strings(string))

