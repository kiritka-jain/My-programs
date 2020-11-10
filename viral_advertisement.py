no_of_days = int(input())
shared = 5
liked = 0
cumulative = 0
for _ in range(no_of_days):
    liked = shared//2
    cumulative += liked
    shared = liked *3
print(cumulative)
