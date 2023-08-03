#Password Generator using string:
import random
Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*','(',')','?']
print("Welcome to the password Generator!")
no_of_letters = int(input("How many letters do you  want:\n"))
no_of_numbers = int(input("How many numbers do you want:\n"))
no_of_symbols = int(input("How many symbols do you want:\n"))
password = ""
for char in range(1, no_of_letters+1):
    password += random.choice(Letters)
for char in range(1,no_of_numbers+1):
    password += random.choice(Numbers)
for char in range(1,no_of_symbols+1):
    password += random.choice(Symbols)
print(password)
 
# And also We can do this same using list:
import random
Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*','(',')','?']
print("Welcome to the password Generator!")
no_of_letters = int(input("How many letters do you  want:\n"))
no_of_numbers = int(input("How many numbers do you want:\n"))
no_of_symbols = int(input("How many symbols do you want:\n"))
password_list = []
for char in range(1, no_of_letters+1):
    password_list.append(random.choice(Letters))
for char in range(1,no_of_numbers+1):
    password_list+= random.choice(Numbers)
for char in range(1,no_of_symbols+1):
    password_list += random.choice(Symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your Password is {password}")