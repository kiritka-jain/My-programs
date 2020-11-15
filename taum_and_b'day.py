def cost_calculator(black,white,black_cost,white_cost,conversion_cost):
    total_cost = black*(min(black_cost,(white_cost+conversion_cost)))+white*(min(white_cost,(black_cost+conversion_cost)))
    return total_cost


total_test_cases = int(input())
for _ in range(total_test_cases):
    black,white = list(map(int,input().split()))
    black_cost,white_cost,conversion_cost = list(map(int,input().split()))
    print(cost_calculator(black,white,black_cost,white_cost,conversion_cost))

