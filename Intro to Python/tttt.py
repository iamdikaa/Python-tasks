import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_numbers = int(input(f"How many numbers would you like?\n"))



password = []
for choice in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)