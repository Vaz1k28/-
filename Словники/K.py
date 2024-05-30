def count_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    result = []

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        result.append(str(word_count[word]))
        word_count[word] += 1

    return ' '.join(result)

input_data = [
    "one two one two three",
    "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
]

for data in input_data:
    print(count_occurrences(data))
