#Password Generator Project
from posixpath import split
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''
VERSION 1, MI VERISON 

size_letters = len(letters) #tamaño de lista de letras
size_numbers = len(numbers) #tamaño de lista de numeros
size_symbols = len(symbols) #tamaño de lista de simbolos

#password_letters = ""
#password_symbols = ""
#password_numbers = "" 

password = ""

for l in range(1, nr_letters+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    letter = random.choice(letters)
    password += letter

for n in range(1, nr_numbers+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    number = random.choice(numbers)
    password += number

for s in range(1, nr_symbols+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    symbol = random.choice(symbols)
    password += symbol

print(password)


'''

#VERSION 2

lenght_password = nr_letters + nr_symbols + nr_numbers

size_letters = len(letters) #tamaño de lista de letras
size_numbers = len(numbers) #tamaño de lista de numeros
size_symbols = len(symbols) #tamaño de lista de simbolos


password = []

for l in range(1, nr_letters+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    letter = random.choice(letters)
    position = random.randint(0,len(password))
    password.insert(position, letter)

for n in range(1, nr_numbers+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    number = random.choice(numbers)
    position = random.randint(0,len(password))
    password.insert(position, number)

for s in range(1, nr_symbols+1):
    #letter = letters[random.randint(0, size_letters)] #letra random
    #password_letters.append(letter)
    symbol = random.choice(symbols)
    position = random.randint(0,len(password))
    password.insert(position, symbol)

final_password = ""
for element in password:
    final_password += element

print(f"Your password is: {final_password}")


#otra forma de cambiar el orden de la lista hubiera sido con la funcion shuffle del metodo
#random, asi random.shuffle(password) donde password es la lista que queremos cambiar