def minimum_distance(size,arr):
    distance =[]
    for index in range(size):
        for index_2 in range(index+1,size):
            if arr[index] == arr[index_2]:
                distance_diff= abs(index_2 - index)
                distance.append(distance_diff)
    if distance == []:
        return -1
    else:
        return min(distance)


size_of_array = int(input())
arr = list(map(int,input().split()))
minimum_distance(size_of_array,arr)
result = minimum_distance(size_of_array,arr)
print(result)







