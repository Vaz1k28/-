def count_unique_numbers(numbers):
  unique_numbers = set(numbers)
  return len(unique_numbers)


numbers = [1, 2, 3, 2, 1]
unique_count = count_unique_numbers(numbers)
print(f"Кількість унікальних чисел: {unique_count}")
