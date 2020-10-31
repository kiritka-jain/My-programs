def serving_lane_width(start,end,array):
    possible_width =[]
    for index in range(start,end+1):
        possible_width.append(array[index])
    return min(possible_width)






width_measurement,test_cases = list(map(int,input().split()))
width_array = list(map(int,input().rstrip().split()))
for _ in range(test_cases):
    start_index,end_index = list(map(int,input().rstrip().split()))
    print(serving_lane_width(start_index,end_index,width_array))
