def choclate_squares(choclate_bar_length,no_on_choclate_square,birth_day,birth_month):
    count = 0
    if choclate_bar_length == 1:
        if no_on_choclate_square[0] == birth_day:
            return 1
    else:
        for square in range(choclate_bar_length-1):
            square_count = no_on_choclate_square[square:(square+birth_month)]
            square_sum =sum(square_count)
            if square_sum == birth_day:
                count+=1
        return count


choclate_bar_length = int(input())
no_on_choclate_square =list(map(int,input().split()))
birth_day,birth_month = list(map(int,input().split()))
print(choclate_squares(choclate_bar_length,no_on_choclate_square,birth_day,birth_month))



