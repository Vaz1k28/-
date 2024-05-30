list1 = [1, 2, 3, 3, 2]
list2 = [2]


matching_count = 0

for num1 in list1:

    if num1 in list2:
        matching_count += 1

print(matching_count)
