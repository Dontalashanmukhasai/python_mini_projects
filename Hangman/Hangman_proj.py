import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
from hangman_words import words_list
lives = 6
choosen_word = random.choice(words_list)
display = []
for _ in range(len(choosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("guess ur letter:").lower()
    if guess in display:
        print(f"you have already guessed the word{guess}")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")

    if guess not in choosen_word:
        print(f"you guessed {guess} that not in the word. you lose a life")
        lives -=1
    if lives == 0:
        print("You loose, Game over!")
    print(stages[lives])