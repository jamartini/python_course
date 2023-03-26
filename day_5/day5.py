import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Fixed Order

letters_part = []
for i in range(0, nr_letters):
    letters_part.append(letters[random.randint(0, int(len(letters) - 1))])

symbols_part = []
for i in range(0, nr_symbols):
    symbols_part.append(symbols[random.randint(0, int(len(symbols) - 1))])

numbers_part = []
for i in range(0, nr_numbers):
    numbers_part.append(numbers[random.randint(0, int(len(numbers) - 1))])

letters_str = ''.join(letters_part)
symbols_str = ''.join(symbols_part)
numbers_str = ''.join(numbers_part)
pw_list = [letters_str, symbols_str, numbers_str]
password = ''.join(pw_list)
print(password)

letters_part = []
for i in range(0, nr_letters):
    letters_part.append(letters[random.randint(0, int(len(letters) - 1))])

symbols_part = []
for i in range(0, nr_symbols):
    symbols_part.append(symbols[random.randint(0, int(len(symbols) - 1))])

numbers_part = []
for i in range(0, nr_numbers):
    numbers_part.append(numbers[random.randint(0, int(len(numbers) - 1))])

letters_str = ''.join(letters_part)
symbols_str = ''.join(symbols_part)
numbers_str = ''.join(numbers_part)
pw_list = [letters_str, symbols_str, numbers_str]
password = ''.join(pw_list)
password = [*password]
random.shuffle(password)
shuffled_password = ''.join(password)
print(shuffled_password)
