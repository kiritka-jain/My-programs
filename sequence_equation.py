total_integers = int(input())
sequence = list(map(int,input().rstrip().split()))
index_2 =[]
for x in range(1,total_integers+1):
    for index in range(len(sequence)):
        if sequence[index] == x:
            index_2.append((index+1))
for value in index_2:
    for y in range(len(sequence)):
        if sequence[y] == value:
            print(y+1)








