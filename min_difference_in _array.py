arr_size = int(input())
array = list(map(int,input().rstrip().split()))
array = sorted(array)
min_diff =[]
for elem in range(arr_size-1):
    difference = array[elem+1]-array[elem]
    min_diff.append(difference)
print(min(min_diff))
