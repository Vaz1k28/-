text = """
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
"""

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_2 = [(count, word) for word, count in word_count.items()]

word_2.sort(reverse=True)

for freq, word in word_2:
    print(word)