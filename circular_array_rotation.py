array_elem,rotation_count,queries = list(map(int,input().split()))
array = list(map(int,input().split()))
for _ in range(queries):
    index = int(input())
    print(array[(index-rotation_count)%array_elem])


