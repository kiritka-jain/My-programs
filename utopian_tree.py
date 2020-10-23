def utopian_tree(cycles):
    height = 1
    for cycle in range(cycles+1):
        if cycle == 0:
            height = 1
        elif cycle % 2 != 0:
            height = height*2
        elif cycle % 2 == 0:
            height +=1
    return print(height)


total_test_cases = int(input())
for _ in range(total_test_cases):
    no_of_cycle = int(input())
    result = utopian_tree(no_of_cycle)


