def count_apple_ornage(house_start,house_end, apple_tree,orange_tree,apples,oranges):
    total_apples = 0
    total_oranges = 0
    for apple_dis in apples:
        if(apple_dis+apple_tree)>=house_start and ((apple_dis+apple_tree))<=house_end:
            total_apples+=1
    for orange_dis in oranges:
        if house_start<=(orange_tree +orange_dis)and (orange_tree +orange_dis)<=house_end:
           total_oranges+=1
    print(total_apples)
    print(total_oranges)





house_start,house_end = map(int,input().split())
apple_tree,orange_tree = map(int,input().split())
apple_len,orange_len = map(int,input().split())
apples = list(map(int,input().split()))
oranges = list(map(int,input().split()))


count_apple_ornage(house_start,house_end,apple_tree,orange_tree,apples,oranges)





