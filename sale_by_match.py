no_of_socks = int(input())
socks = list(map(int,input().split()))
total_socks = {}
total_pair =0
for sock in socks:
    if sock not in total_socks:
        total_socks[sock] = 1
    else:
        total_socks[sock]+=1
for pairs in total_socks:
    total_pair += int((total_socks[pairs])/2)
print(total_pair)



