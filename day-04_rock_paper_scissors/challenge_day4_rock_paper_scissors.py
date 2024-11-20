#Final Project Day 4 - Rock-Paper-Scissors Game
#14nd October 2024
#Her link: https://appbrewery.github.io/python-day4-demo/
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

print("Welcome to Juan's Game - Rock-Paper-Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0,2)

if user_choice == 0:
    print("You chose Rock")
    print(rock)
elif user_choice == 1:
    print("You chose Paper")
    print(paper)
elif user_choice == 2:
    print("You chose Scissors")
    print(scissors)

print("\n" + "-----------------------------" + "\n")

if user_choice in(0,1,2):
    if computer_choice == 0:
        print("The computer chose Rock")
        print(rock)
    elif computer_choice == 1:
        print("The computer chose Paper")
        print(paper)
    else:
        print("The computer chose Scissors")
        print(scissors)

#Checking Result
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice not in(0,1,2):
    print("You typed a wrong input")
else:
    print("You lost!")