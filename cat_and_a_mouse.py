def cat_mouse_catch(cat_a,cat_b,mouse):
    if abs(mouse-cat_a)> abs(mouse-cat_b):
        return print("Cat B")
    elif abs(mouse-cat_a)< abs(mouse-cat_b):
        return print("Cat A")
    else:
        return print("Mouse C")

no_of_queries = int(input())
for _ in range(no_of_queries):
        position = input().split()

        cat_a = int(position[0])

        cat_b = int(position[1])

        mouse = int(position[2])

        result = cat_mouse_catch(cat_a,cat_b,mouse)



