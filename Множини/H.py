def answer_andriy(n, questions):
    possible_numbers = set(range(1, n + 1))
    responses = []

    for question in questions:
        question_numbers = set(question)
        remaining_if_yes = possible_numbers.intersection(question_numbers)
        remaining_if_no = possible_numbers.difference(question_numbers)

        if len(question_numbers) == len(possible_numbers) / 2:
            responses.append("NO")
            possible_numbers = remaining_if_no
        elif len(remaining_if_yes) >= len(remaining_if_no):
            responses.append("YES")
            possible_numbers = remaining_if_yes
        else:
            responses.append("NO")
            possible_numbers = remaining_if_no

    return responses, sorted(possible_numbers)



n = 10
questions = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]]

answers, possible_numbers = answer_andriy(n, questions)

print("Відповіді Андрія:")
for answer in answers:
    print(answer)

print("Можливі числа:", possible_numbers)
