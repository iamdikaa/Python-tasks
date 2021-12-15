import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols= int(input("How many letters would you like in your password?\n")) 

numbers_samp = random.sample(numbers, k = nr_numbers)
letters_samp = random.sample(letters, k = nr_letters)
symbols_samp = random.sample(symbols, k = nr_symbols)


password = ""
generator = ""
for numb_ers in numbers_samp:
    password +=numb_ers

for numb_ers in letters_samp:
    password +=numb_ers

for numb_ers in symbols_samp:
    password +=numb_ers

print(password)


length_of_all = len(password)

num_generator = random.sample(password, k=length_of_all)
print(num_generator)

for random_num in num_generator:
    generator +=random_num
print(f'Your Password is: {generator}')



