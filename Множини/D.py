def number(input_string):
    results = []

    seen_numbers = set()

    words = input_string.split()


    for word in words:
        number = int(word)

        if number in seen_numbers:
            results.append("YES")
        else:
            results.append("NO")
            seen_numbers.add(number)

    return results


input_string = "1 2 3 1 4 5"
results = number(input_string)

for result in results:
    print(result)
