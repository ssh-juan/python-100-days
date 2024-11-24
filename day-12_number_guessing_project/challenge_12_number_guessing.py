#Final Project Day 12 - Number Guessing Game
#24nd November 2024
#Her link: https://appbrewery.github.io/python-day12-demo

#Easy Level = 10 attempts
#Hard Level = 5 attempts


print("Welcome to my Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")
    guess = input("Make a guess: ")
else:
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")
    guess = input("Make a guess: ")