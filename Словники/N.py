def common_words(text):

    words = text.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_count = max(word_count.values())
    most_common_words = [word for word, count in word_count.items() if count == max_count]

    most_common_words.sort()
    return most_common_words[0]

text = "apple orange banana banana orange"

print(common_words(text))
