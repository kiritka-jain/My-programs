from collections import  Counter

array_size = int(input())
array = list(map(int,input().rstrip().split()))
final_ans =[]
frequency = Counter(array)
for num in frequency:
    if num+1 in array:
        answer = frequency[num]+frequency[num+1]
        final_ans.append(answer)
    else:
        final_ans.append(frequency[num])
print(max(final_ans))
