#Final Project Day 14 - Higher or Lower
#28th November 2024
#Her link: https://appbrewery.github.io/python-day14-demo
import random
import art
import game_data
from os import system

score = 0
missed = False

print(art.logo)
while missed == False:
    rand_a = random.randint(0,49)
    rand_b = random.randint(0,49)

    print(f"Compare A: {game_data.data[rand_a]["name"]}, a {game_data.data[rand_a]["description"]}, from {game_data.data[rand_a]["country"]}.")
    print(art.vs)
    print(f"Compare B: {game_data.data[rand_b]["name"]}, a {game_data.data[rand_b]["description"]}, from {game_data.data[rand_b]["country"]}.")

    #compare(choice, rand_a, rand_b, score, missed)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    system("cls")
    if choice in ("A","a"):
        if game_data.data[rand_a]["follower_count"] > game_data.data[rand_b]["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            missed = True
    elif choice in ("B", "b"):
        if game_data.data[rand_b]["follower_count"] > game_data.data[rand_a]["follower_count"]:
            score += 1
            print(f"You're Right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            missed = True