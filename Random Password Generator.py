import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["1","2","3","4","5,","6","7","8","9","0"]
symbols = ["!","_","-","?","&"]
print("Welcome to password generator")

amount_letters = int(input("how many letters would you like to use in your password: "))
amount_numbers = int(input("how many numbers would you like to use in your password: "))
amount_symbols = int(input("how many symbols would you like to use in your password: "))

list = []

for char in range(1,amount_letters+1):
    list.append(random.choice(letters))
    
for char in range(1,amount_numbers+1):
    list.append(random.choice(numbers))
    
for char in range(1,amount_symbols+1):
    list.append(random.choice(symbols))
    

random.shuffle(list)

password = ""

for q in list:
    password = q + password
    
    
print(password)
