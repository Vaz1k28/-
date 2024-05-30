def read_dictionary():
    dictionary = {}
    n = int(input())
    for _ in range(n):
        word = input().strip()
        dictionary[word] = set(input().split())
    return dictionary


def check_homework(dictionary):
    text = input().strip().split()
    errors = 0
    for word in text:
        if word.lower() in dictionary:
            if word.capitalize() != word:
                if word.capitalize() not in dictionary[word.lower()]:
                    errors += 1
        else:
            if word.capitalize() == word:
                errors += 1
    return errors


dictionary = read_dictionary()

errors = check_homework(dictionary)

print(errors)