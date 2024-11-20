#Final Project Day 9 - Blind Auction Program
#05nd November 2024
#Her link: https://appbrewery.github.io/python-day9-demo
from os import system
import auction_logo
print(auction_logo.logo)
print("Welcome to Juan's Blind Auction Program! =)")

data = {
    "name": [],
    "bid": [],
}

rerun = True
while rerun:
    # TODO-1: Ask the user for input
    data["name"].append(input("What's your name? "))
    print(data)

    data["bid"].append(input("What's your bid? $"))
    print(data)

    rerun_input = input("Are there any other bidders? Type 'yes' or 'no'\n")

    # TODO-3: Whether if new bids need to be added
    if rerun_input == "yes":
        system("cls")
    elif rerun_input == "no":
        rerun = False
    # TODO-2: Save data into dictionary {name: price}

# TODO-4: Compare bids in dictionary
highest_bid = 0
rotate = 0
for bid in data["bid"]:
    if bid > highest_bid:
        winner = data["name"][rotate]
        highest_bid = bid
    rotate += 1

# # Usando zip() para itear sobre nomes e bids simultaneamente
# for name, bid in zip(data["name"], data["bid"]):
#     if bid > highest_bid:
#         winner = name
#         highest_bid = bid

print(f"The winner is {winner} with a bid of ${highest_bid}")