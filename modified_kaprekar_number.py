import math

lower_limit = int(input())
upper_limit = int(input())
final_answer = []
for num in range(lower_limit,upper_limit+1):
    square_num = str(num*num)
    digit_len = len(square_num)
    if digit_len == 1:
        if int(square_num) == num:
            final_answer.append(num)
    elif digit_len%2 == 0:
        digit_len= int(digit_len/2)
        left_part = square_num[0:digit_len]
        right_part = square_num[digit_len:]
        if int(left_part)+int(right_part) == num:
            final_answer.append(num)
    else:
        digit_len =math.floor(digit_len/2)
        left_part = square_num[0:digit_len]
        right_part = square_num[digit_len:]
        if int(left_part)+int(right_part) == num:
            final_answer.append(num)
if len(final_answer) >0:
    print(*(final_answer))
else:
    print("INVALID RANGE")




