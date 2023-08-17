import random
def deal_card():
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

user_cards = []
computer_cards = []
for i in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def calculate_score(cards):
  return sum(cards)
  
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"your card: {user_cards} , your present score: {user_score} ")
print(f"computer's first card: {computer_cards[0]}")

another_card = input("type 'yes' to draw another card or 'no' to pass to computer:" )
if another_card == "yes":
    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    if user_score>21:
        if computer_score<21:
            print("computer won!")
            print(f"your score is {user_score} and computer score {computer_score}")
        else:
          print("you lost")
          print(f"your score is {user_score} and computer score {computer_score}")
    elif computer_score>21:
       if user_score <21:
            print("you won!")
            print(f"your score is {user_score} and computer score {computer_score}")
    elif user_score == 21:
       print("You won")
       print(f"your score is {user_score} and computer score {computer_score}")
    elif computer_score > 21 or (user_score < 21 and user_score > computer_score): 
       print("you won!")
       print(f"your score is {user_score} and computer score {computer_score}")
    elif computer_score == 21 or user_score < computer_score:
       print("computer won!")
       print(f"your score is {user_score} and computer score {computer_score}")
    elif user_score == computer_score:
       print("Draw")
       print(f"your score is {user_score} and computer score {computer_score}")

else:
   if computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
   if user_score == 21:
        print("user_win")
        print(f"your score is {user_score} and computer score {computer_score}")
   elif computer_score > 21 or (user_score < 21 and user_score > computer_score):
        print("user_win")
        print(f"your score is {user_score} and computer score {computer_score}")
   elif computer_score == 21 or user_score < computer_score:
        print("computer won")
        print(f"your score is {user_score} and computer score {computer_score}")
   elif user_score == computer_score:
        print("draw")
        print(f"your score is {user_score} and computer score{computer_score}")

