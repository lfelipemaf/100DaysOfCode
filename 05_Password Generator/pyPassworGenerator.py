#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
#Eazy Level - Order not randomised:
#e.g. 4 letter_file, 2 symbol, 2 number = JduE&!91
for l in range(1,nr_letters+1):
    letter = random.choice(letters)
    password_list.append(letter)
for n in range(1,nr_numbers+1):
    number = random.choice(numbers)
    password_list.append(number)
for s in range(1,nr_symbols+1):
    symbol = random.choice(symbols)
    password_list.append(symbol)
password = ''.join(password_list)
print(f"Easy password: {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter_file, 2 symbol, 2 number = g^2jk8&P
password_list = []
for l in range(1,nr_letters+1):
    letter = random.choice(letters)
    i = random.randint(0,len(password_list))
    password_list.insert(i,letter)
for n in range(1,nr_numbers+1):
    number = random.choice(numbers)
    i = random.randint(0,len(password_list))
    password_list.insert(i,number)
for s in range(1,nr_symbols+1):
    symbol = random.choice(symbols)
    i = random.randint(0, len(password_list))
    password_list.insert(i, symbol)
password = ''.join(password_list)
print(f"Hard password: {password}")