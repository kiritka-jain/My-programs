def counting_sort(total_items,array):
    result = []
    count = 0
    for index in range(100):
       result.append(0)
    for elem in array:
        result[elem] +=1
    return result




total_items = int(input())
array = list(map(int,input().rstrip().split()))
print(*(counting_sort(total_items,array)))
