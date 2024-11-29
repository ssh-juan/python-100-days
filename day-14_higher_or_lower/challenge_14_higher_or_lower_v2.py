#Final Project Day 14 - Higher or Lower
#28th November 2024
#Her link: https://appbrewery.github.io/python-day14-demo

#v2 using function compare()

import random
import art
import game_data
from os import system

score = 0
missed = False

def compare(rand_a, rand_b):
    global score, missed
    choice = input("Who has more followers? Type 'A' or 'B': ")
    system("cls")
    if choice in ("A","a"):
        if game_data.data[rand_a]["follower_count"] > game_data.data[rand_b]["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
            return score
        else:
            missed = True
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, missed
    elif choice in ("B", "b"):
        if game_data.data[rand_b]["follower_count"] > game_data.data[rand_a]["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
            return score
        else:
            missed = True
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, missed

while missed == False:
    rand_a = random.randint(0,49)
    rand_b = random.randint(0,49)

    print(art.logo)
    print(f"Compare A: {game_data.data[rand_a]["name"]}, a {game_data.data[rand_a]["description"]}, from {game_data.data[rand_a]["country"]}.")

    print(art.vs)
    print(f"Compare B: {game_data.data[rand_b]["name"]}, a {game_data.data[rand_b]["description"]}, from {game_data.data[rand_b]["country"]}.")

    compare(rand_a, rand_b)