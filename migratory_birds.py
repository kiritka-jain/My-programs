total_birds_spotted = int(input())
birds = list(map(int,input().split()))
freq_of_birds = {}
most_frequent_birds = []
for bird in birds:
    if bird not in freq_of_birds:
        freq_of_birds[bird] = 1
    else:
        freq_of_birds[bird]+=1
maximum_freq = (max(freq_of_birds.values()))
for type,freq in freq_of_birds.items():
    if freq_of_birds[type] == maximum_freq:
        most_frequent_birds.append(type)
print(min(most_frequent_birds))




