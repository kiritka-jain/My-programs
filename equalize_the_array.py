from collections import Counter

total_elem = int(input())
array = list(map(int,input().rstrip().split()))
elem_freq = Counter(array)
freq =[]
for i in elem_freq:
    freq.append(elem_freq[i])
print(total_elem - max(freq))




