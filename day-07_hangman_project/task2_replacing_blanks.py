#Step 2 - Replace placeholder with Guesses
import random

word_list = ['aardvark', "baboon", "camel"]

#1 - Randomly choose a word from the world_list and assign it to a variable called 'chosen_word'. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

#2 - Replacing letters with placeholder
placeholder = ""
for letter in (chosen_word):
    placeholder += "_"
print(placeholder)

#3 - Ask the user to guess a letter and assign their answer to a variable called 'guess'. Make 'guess' lowercase.
guess = input("Guess a letter: ").lower()

#4 - Create a "display" that puts the 'guess' letter in the right positions and '_' in the rest of the string.
display = ""

for letter in (chosen_word):
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)