total_toys,total_amt = list(map(int,input().split()))
toys_price_list = list(map(int,input().rstrip().split()))
sorted_toys_price_list = sorted(toys_price_list)
toys = -1
total_price = 0
for price in sorted_toys_price_list:
    if total_price <= total_amt:
        total_price+=price
        toys+=1
print(toys)


