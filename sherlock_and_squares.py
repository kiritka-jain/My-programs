import math

test_cases = int(input())
for _ in range(test_cases):
    start,end = list(map(int,input().split()))
    range_start = math.ceil(math.sqrt(start))
    range_end = math.floor(math.sqrt(end))
    print((range_end-range_start)+1)


