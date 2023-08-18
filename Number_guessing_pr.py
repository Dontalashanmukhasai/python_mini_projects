import random
print("Welcome to the Number guessing Game.")
number = random.randint(1,100)
print("I'm thinking of a number between 1 to 100")
user_choose = input("choose a difficulty. type 'easy' or 'hard' : ")
if user_choose == "easy":
    print("you have 10 attempts to guess the number.")
    for i in range(0,11):
        guess = int(input("guess the number:"))
        attempts = 10-i
        if guess > number:
            print("Too High!")
            print(f"you have {attempts} to guess the number")
        elif guess<number:
            print("Too low")
            print(f"you have {attempts} to guess the number")
        else:
            print("you got it! the number is {number}")
        if attempts==0:
            print("you have ran out of guess")
            print("you loose!")
            print("Better luck next time.")        
elif user_choose == "hard":
    print("you have 5 attempts to guess the number.")
    for i in range(1,6):
        guess = int(input("guess the number: "))
        attempts = 5-i
        if guess > number:
            print("Too High!")
            print(f"you have {attempts} to guess the number")
        elif guess<number:
            print("Too low")
            print(f"you have {attempts} to guess the number")
        else:
            print("you got it! the number is {number}")
        if attempts==0:
            print("you have ran out of guess")
            print("you loose!")
            print("Better luck next time.") 

else:
    print("you have entered wrong input.")