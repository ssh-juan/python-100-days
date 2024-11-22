#Final Project Day 11 - Blackjack Game
#21st November 2024
#Her link: https://appbrewery.github.io/python-day11-demo

#My solution only watching the first explanation
import random
from os import system
import art

run = True
while run:
    user_cards = []
    computer_cards = []
    end = False
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play in ("Y","y"):
        system("cls")
        print(art.logo)
        for num in range(2):
            user_cards.append(random.randint(1,10))
        #print(user_cards)
        computer_cards.append(random.randint(1,10))
        #print(computer_cards)

        print(f"Your cards: {user_cards}. Your current score: " + str(sum(user_cards)))
        print(f"Computer's first card: {computer_cards}")

        get_card = input("Type 'y' to get another card, or type 'n' to pass: ")
        while get_card in ("Y","y"):
            user_cards.append(random.randint(1,10))

            if sum(user_cards) > 21:
                print(f"Your final hand is: {user_cards}. Your final score: " + str(sum(user_cards)))
                print(f"Computer's final hand: {computer_cards}. Final score: " + str(sum(computer_cards)))
                print("You went over 21. You lose!")

                get_card = "n"
                end = True
            elif sum(user_cards) == 21:
                print(f"Your final hand is: {user_cards}. Your final score: " + str(sum(user_cards)))
                print(f"Computer's final hand: {computer_cards}. Final score: " + str(sum(computer_cards)))
                print("You got 21. You win!")

                get_card = "n"
                end = True
            else:
                print(f"Your cards: {user_cards}. Your current score: " + str(sum(user_cards)))
                print(f"Computer's first card: {computer_cards}")
                get_card = input("Type 'y' to get another card, or type 'n' to pass: ")
        
        if not end:
            computer_cards.append(random.randint(1,10))

            if sum(computer_cards) > sum(user_cards):
                print(f"Your final hand is: {user_cards}. Your final score: " + str(sum(user_cards)))
                print(f"Computer's final hand: {computer_cards}. Final score: " + str(sum(computer_cards)))
                print("You lose. Computer's hand is greater than yours.")
            elif sum(computer_cards) == sum(user_cards):
                print(f"Your final hand is: {user_cards}. Your final score: " + str(sum(user_cards)))
                print(f"Computer's final hand: {computer_cards}. Final score: " + str(sum(computer_cards)))
                print("It's a draw. Equal hands.")
            else:
                print(f"Your final hand is: {user_cards}. Your final score: " + str(sum(user_cards)))
                print(f"Computer's final hand: {computer_cards}. Final score: " + str(sum(computer_cards)))
                print("You win! Your hand is greater than computer.")
        
    else:
        run = False
        print("\nOk, you've decided not to play.\nBye!")