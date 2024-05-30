def number(n, queries, answers):

    possible_numbers = set(range(1, n + 1))

    for query, answer in zip(queries, answers):
        query_set = set(query)
        if answer == "YES":
            possible_numbers &= query_set
        else:
            possible_numbers -= query_set

    return sorted(possible_numbers)


n = 10
queries = [[1, 2, 3, 4, 5], [4, 6, 8, 10]]
answers = ["YES", "NO"]

possible_numbers = number(n, queries, answers)
print(possible_numbers)

