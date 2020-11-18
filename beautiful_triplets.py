def beautiful_triplets(difference,sequence):
    triplet =0
    for num in sequence:
        if num+difference in sequence and num + 2*difference in sequence:
            triplet+=1
    return triplet



sequence_len,difference = list(map(int,input().split()))
sequence = list(map(int,input().rstrip().split()))

print(beautiful_triplets(difference,sequence))
