cube = lambda x:x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    a= 0
    b = 1
    c = 0
    fibonacci_series=[]
    for i in range(n):
        if i == 0:
            fibonacci_series.append(a)
        elif i == 1:
            fibonacci_series.append(b)
        else:
            c=a+b
            fibonacci_series.append(c)
            a = b
            b = c
    return fibonacci_series
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
