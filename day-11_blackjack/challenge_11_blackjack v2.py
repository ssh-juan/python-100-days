#Final Project Day 11 - Blackjack Game
#21st November 2024
#Her link: https://appbrewery.github.io/python-day11-demo

#Doing her way
import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21: #"fixing" error, because it could have chosen number 11 twice
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over 21. You lose!"
    elif c_score > 21:
        return "Opponent went over 21. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
    computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or type 'n' to pass: ")
            if user_should_deal in ("Y","y"):
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}. Final Score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        print("\n" * 20)
        play_game()

play_game()