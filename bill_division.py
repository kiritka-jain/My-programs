no_of_items,anna_not_eat = map(int,input().split())
bill = list(map(int,input().split()))
brain_charged = int(input())
combined_items = []
total_combined_bill = 0
for items in range(no_of_items):
    if items!= anna_not_eat:
        combined_items.append(bill[items])
for item in combined_items:
    total_combined_bill +=item
brain_actual = total_combined_bill/2
if brain_actual==brain_charged:
    print("Bon Apetite")
else:
    print(int(brain_charged-brain_actual))


