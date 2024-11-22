#Final Project Day 4 - Rock-Paper-Scissors Game
#14nd October 2024
#Her link: https://appbrewery.github.io/python-day4-demo/
#This code is how she solved the problem.
#I putted it here because she used Lists and I don't.
import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game_images = [rock, paper, scissors]

print("Welcome to Juan's Game - Rock-Paper-Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number. You lost!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lost!")
elif computer_choice > user_choice:
    print("You lost!")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")