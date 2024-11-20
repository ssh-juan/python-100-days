#Step 4 - Keeping track of player's lives
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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

word_list = ['aardvark', "baboon", "camel"]

#Create a variable called 'lives' to keep track of the user lives.
#Set 'lives' = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in (chosen_word):
    placeholder += "_"
print(placeholder)


game_over = False
lives = 6
right_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in (chosen_word):
        if letter == guess:
            display += letter
            right_letters.append(letter)
        elif letter in right_letters:
            display += letter
        else:
            display += "_"

#2. If guess is not a letter in 'chosen_word', decrease lives by 1.
    if guess not in chosen_word:
        lives -= 1

#3. Print the ASCII art from the correspondent stage number of lives.
    print(stages[lives])
    print(f"Lives = {lives}")
    print(display)

    if lives == 0:
        print("You lose!")
        game_over = True

    if "_" not in display:
      print("You win!")
      game_over = True