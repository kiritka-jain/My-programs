import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_score =0
    bob_score = 0
    for i in range(3):
        if a[i]>b[i]:
            alice_score+=1
        elif a[i]<b[i]:
            bob_score+=1
    print(alice_score,bob_score)


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)

