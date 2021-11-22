numbers = [20, 20, 20, 30, 40, 40, 50, 50, 50]

unique_numbers = [el for i, el in enumerate(numbers) if i == numbers.index(el)]

print(unique_numbers)