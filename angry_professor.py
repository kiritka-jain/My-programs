no_of_test_cases = int(input())
for _ in range(no_of_test_cases):
    ttl_stud_arrival,threshold = list(map(int,(input().split())))
    arrival_time_each_stud = list(map(int,input().split()))
    stud_on_time = 0
    for time in arrival_time_each_stud:
        if time <= 0:
            stud_on_time += 1
        else:
            continue
    if stud_on_time >= threshold:
        print("NO")
    else:
        print("YES")
