text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."

words = text.split()
words = [word.lower() for word in words]

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

unique_words = len(word_counts)
print(unique_words)
