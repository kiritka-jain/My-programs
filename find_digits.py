def result(integer):
    count = 0
    number_digits = str(integer)
    for num in number_digits:
        if int(num) == 0:
            continue
        if integer%int(num) == 0:
            count+=1
    return count


test_cases = int(input())
for _ in range(test_cases):
    number = int(input())
    print(result(number))
