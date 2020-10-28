alphabet_heights = list(map(int,input().rstrip().split()))
word = input()
word_heights = []
for character in word:
    places = (ord(character)-97)
    word_height = alphabet_heights[places]
    word_heights.append(word_height)
print(max(word_heights)*len(word_heights))







