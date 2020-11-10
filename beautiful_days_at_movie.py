starting_day,ending_day,divisor = list(map(int,input().split()))
beautiful_day = 0
for date in range(starting_day,ending_day+1):
    date = str(date)
    reverse_day = date[::-1]
    if abs(int(date)-int(reverse_day))% divisor == 0:
        beautiful_day +=1
print(beautiful_day)


