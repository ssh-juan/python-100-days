#Step 3 - Checking if the Player has Won
import random

word_list = ['aardvark', "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in (chosen_word):
    placeholder += "_"
print(placeholder)

# 1 - Use a while loop to let the user guess again

game_over = False
right_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    # 2 - Change the 'for' loop so that you keep the previous correct letters
    for letter in (chosen_word):
        if letter == guess:
            display += letter
            right_letters.append(letter)
        elif letter in right_letters:
            display += letter
        else:
            display += "_"
    
    # for char in (display):
    #     if char != "_" and right_letters != "_":
    #         list = char

    print(display)

    # if "_" not in display:
    #     game_over = True
    #     print("You win!")