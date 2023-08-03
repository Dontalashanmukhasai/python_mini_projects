import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock,paper,scissor]
user_input = int(input(" what choice do you want? type 0 for Rock ,1 for paper or 2 for scissor:\n "))
print(game_images[user_input])
computer_choice = random.randint(0,2)
print(f"computer choose:")
print(game_images[computer_choice])

if(user_input == 0 and computer_choice == 2):
    print("you wins!")
if(user_input == 2 and computer_choice == 0):
    print("you loose")
elif(user_input<computer_choice):
    print("you loose")
elif(user_input>computer_choice):
    print("you win!")
elif(computer_choice == user_input):
    print("Its Draw")
elif(user_input>2 or user_input<0):
    print("You typed an invalid number")