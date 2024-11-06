#Final Project Day 9 - Blind Auction Program
#05nd November 2024
#Her link: https://appbrewery.github.io/python-day9-demo
from os import system
import auction_logo
print(auction_logo.logo)
print("Welcome to Juan's Blind Auction Program! =)")

people = {
    "name": [],
    "bid": [],
}

rerun = "yes"
while rerun == "yes":
    # TODO-1: Ask the user for input
    people["name"].append(input("What's your name? "))
    print(people)

    people["bid"].append(input("What's your bid? $"))
    print(people)

    rerun = input("Are there any other bidders? Type 'yes' or 'no'\n")

    # TODO-3: Whether if new bids need to be added
    if rerun == "yes":
        system("cls")
    # TODO-2: Save data into dictionary {name: price}

# TODO-4: Compare bids in dictionary
highest_bid = 0
for key in people:
    if key > highest_bid:
        winner = people
        highest_bid = key

print(f"The winner is {winner} with a bid of ${highest_bid}")