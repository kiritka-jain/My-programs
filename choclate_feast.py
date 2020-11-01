def choclate_feast(money_spent,choclate_cost,wrappers_to_exchange):
    choclates = int(money_spent/choclate_cost)
    wrappers = choclates
    total = choclates
    for _ in range(choclates):
        if wrappers!=1:
            new_choclates = int(wrappers/wrappers_to_exchange)
            wrappers =(wrappers%wrappers_to_exchange) +new_choclates
            total += new_choclates
    return total


test_cases = int(input())
for _ in range(test_cases):
    money_spent,choclate_cost,wrappers_to_exchange = list(map(int,input().split()))
    print(choclate_feast(money_spent,choclate_cost,wrappers_to_exchange))
