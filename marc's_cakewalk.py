total_cupcakes = int(input())
cupcakes_calorie = list(map(int,input().split()))
cupcakes_calorie = sorted(cupcakes_calorie,reverse=True)
calories = 0
for index in range(total_cupcakes):
    calories += (2**index)*cupcakes_calorie[index]
print(calories)


