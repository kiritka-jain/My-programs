def alternating_characters(string):
    string_len = len(string)
    remove = 0
    for index in range(string_len-1):
        if string[index] == string[index+1]:
            remove +=1
    return remove

total_queries = int(input())
for _ in range(total_queries):
    string  = input()
    print(alternating_characters(string))
