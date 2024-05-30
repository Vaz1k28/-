def count_word(a, b):
    with open(a, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = {}
    result = []

    for word in words:
        if word in word_count:
            result.append(word_count[word])
            word_count[word] += 1
        else:
            result.append(0)
            word_count[word] = 1

    with open(b, 'w') as file:
        file.write(' '.join(map(str, result)))

