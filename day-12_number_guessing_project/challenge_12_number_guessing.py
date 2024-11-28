#Final Project Day 12 - Number Guessing Game
#24nd November 2024
#Her link: https://appbrewery.github.io/python-day12-demo

#My solution

#Easy Level = 10 attempts
#Hard Level = 5 attempts
import random
import art

#comparison
def compare(guess, random_num, attempts):
    """Compares the guessed number with the random number, and update variable 'attempts' if needed."""
    if guess == random_num:
        return "win"
    elif int(guess) > random_num:
        attempts -= 1
        if attempts == 0:
            return "Too high and out of attempts. You lose!", attempts
        else:
            return "Too high", attempts
    elif int(guess) < random_num:
        attempts -= 1
        if attempts == 0:
            return "Too low and out of attempts. You lose!", attempts
        else:
            return "Too low", attempts

def game():
    """Runs the game"""
    print(art.logo)
    print("Welcome to my Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_num = random.randint(1,100)
    print(random_num) ##########################
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempts = 10
    else:
        attempts = 5
    while attempts > 1:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result, attempts = compare(guess, random_num, attempts)
        print(result)
        if result == "win":
            break
        #or just return

game()