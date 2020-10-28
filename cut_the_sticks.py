def cut_the_stick(arr_size,stick_length):
    new_array =[]
    for log in stick_length:
        cut = min(stick_length)
        new_log = log - cut
        if new_log >0:
            new_array.append(new_log)
    return new_array



array_size = int(input())
stick_length = list(map(int,input().rstrip().split()))
for _ in range(array_size):
    if len(stick_length) != 0:
        new_arr = (cut_the_stick(array_size,stick_length))
        print(len(stick_length))
        stick_length = new_arr

