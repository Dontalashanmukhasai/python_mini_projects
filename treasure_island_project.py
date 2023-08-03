print('''  __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')
print("Welcome to Treasure Isalnd.")
print("Your Mission is to find the Treasure.")
choice1 = input('you are at cross road , where do you want to go? Type "left" or "right" .').lower()
if(choice1 == "left"):
    coice2 = input('you have come to lake, there is an isalnd in middle of the lake. type "type" to wait for the boat. type "swim" to swim.').lower()
    if(coice2 == "wait"):
        choice3 = input('You have arrived to island,there is a house with 3 different doors,which one do you choose?').lower()
        if(choice3 == "yellow" ):
            print("Congratulations!\n you have won the Game.")
        elif(choice3 == "red"):
            print("there is full of fire, you lost game.")
        elif(choice3 == "blue"):
            print("There are full snakes, You lost the Game.")
        else:
            print("you had choosen which doesnt contain.")
    else:
        print("You got attacked by the angry crocodile, Game over!")
else:
    print("You fell into a hole. Game Over!")