string_to_repeat = input()
substring_lenght_considered = int(input())
string_length = len(string_to_repeat)
count = 0
total = 0
if string_to_repeat == 'a':
    print(substring_lenght_considered)
elif 'a' not in string_to_repeat:
    print(count)
else:
    for char in string_to_repeat:
        if char == 'a':
            count+=1
    full_repeats = int(substring_lenght_considered/string_length)
    remaining_char = substring_lenght_considered-(full_repeats*string_length)
    remaining_string = string_to_repeat[0:remaining_char]
    count = count*full_repeats
    for character in remaining_string:
        if character == 'a':
            total +=1
print(total+count)


