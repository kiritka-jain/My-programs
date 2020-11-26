from collections import  Counter


def string_construction(string):
    unique_char = Counter(string)
    return (len(unique_char))


total_strings = int(input())
for _ in range(total_strings):
    string = input()
    print(string_construction(string))

