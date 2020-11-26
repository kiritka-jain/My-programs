def haloween_sale(initial_price,discount,lower_threshold,total_amount):
    if total_amount < initial_price:
        return 0
    elif total_amount == initial_price or total_amount-initial_price < initial_price:
        return 1
    else:
        n_th_term = int(((lower_threshold-initial_price)/(-discount))+1)
        game = n_th_term
        total = int((n_th_term/2)*(2*initial_price+(n_th_term-1)*(-discount)))
        left_amt = total_amount-total
        more_games = int(left_amt/lower_threshold)
        game+= more_games
        return game

initial_price,discount,lower_threshold,total_amount = list(map(int,input().rstrip().split()))

print(haloween_sale(initial_price,discount,lower_threshold,total_amount))


