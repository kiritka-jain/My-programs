def container_needed(total,weight_list):
    weights = sorted(weight_list)
    min_weight = weights[0]
    count = 1
    for weight in weights:
        if weight >= min_weight+5:
            count +=1
            min_weight = weight
    return count


total_items = int(input())
weight_list = list(map(int,input().rstrip().split()))
print(container_needed(total_items,weight_list))
