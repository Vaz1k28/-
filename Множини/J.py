def count_strikes(N, K, parties):
    strikes = [False] * (N + 1)

    for a, b in parties:
        for day in range(a, N + 1, b):
            weekday = (day - 1) % 7 + 1

            if weekday != 6 and weekday != 7:
                strikes[day] = True

    return sum(strikes)

N = 19
K = 3
parties = [(2, 3), (3, 5), (9, 8)]

print(count_strikes(N, K, parties))
