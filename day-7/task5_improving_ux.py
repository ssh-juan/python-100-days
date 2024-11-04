import random
from hangman_words import word_list
from hangman_arts import stages, logo
# 1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# 3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # 6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # 4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    if guess in correct_letters:
        print(f"You had already guessed letter {guess} before")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # 2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])