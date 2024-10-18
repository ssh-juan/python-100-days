#Step 1 - Picking a Random Word and Checking Answers
import random

word_list = ['aardvark', "baboon", "camel"]

#1 - Randomly choose a word from the world_list and assign it to a variable called 'chosen_word'. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

#2 - Ask the user to guess a letter and assign their answer to a variable called 'guess'. Make 'guess' lowercase.
guess = input("Guess a letter: ").lower()

#3 - Check if the letter the user guessed 'guess' is one of the letters in the 'chosen_word'. Print 'right' if it is, 'wrong if it's not.
# i = 0
# for check in (chosen_word):
#     if guess == chosen_word[i]:
#         print("right")
#         i += 1
#     else:
#         print("wrong")
#         i += 1

# better way below
for letter in (chosen_word):
    if letter == guess:
        print("right")
    else:
        print("wrong")