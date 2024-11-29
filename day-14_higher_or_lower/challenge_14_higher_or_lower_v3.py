#Final Project Day 14 - Higher or Lower
#28th November 2024
#Her link: https://appbrewery.github.io/python-day14-demo

#v3 using 'random.choice' instead of using 'randint'

import random
import art
import game_data
from os import system

score = 0
missed = False

def compare(rand_a, rand_b):
    """Compares the random results and checks it according user's guess"""
    global score, missed
    choice = input("Who has more followers? Type 'A' or 'B': ")
    system("cls")
    if choice in ("A","a"):
        if rand_a["follower_count"] > rand_b["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
            return score
        else:
            missed = True
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, missed
    elif choice in ("B", "b"):
        if rand_b["follower_count"] > rand_a["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
            return score
        else:
            missed = True
            print(f"Sorry, that's wrong. Final score: {score}")
            return score, missed

while missed == False:
    rand_a = random.choice(game_data.data)
    rand_b = random.choice(game_data.data)

    #print(art.logo)
    print(f"Compare A: {rand_a["name"]}, a {rand_a["description"]}, from {rand_a["country"]}.")

    print(art.vs)
    print(f"Compare B: {rand_b["name"]}, a {rand_b["description"]}, from {rand_b["country"]}.")

    compare(rand_a, rand_b)