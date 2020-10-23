def total_price_spent(budget,keyboard_list,drivers_list):
    prices = []
    for keyboard in keyboard_list:
        for drivers in drivers_list:
            price = keyboard + drivers
            prices.append(price)
    prices = sorted(prices)
    for highest in reversed(range(len(prices))):
        if prices[highest] <= budget:
            return prices[highest]

    return -1

budget,keyboard_model,drive_model = (list(map(int,input().split())))
keyboard_prices =list(map(int,input().split()))
drivers_prices = list(map(int,input().split()))

print(total_price_spent(budget,keyboard_prices,drivers_prices))

