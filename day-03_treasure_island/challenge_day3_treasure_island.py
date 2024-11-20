#Final Project Day 3 - Treasure Island - Choose your own adventure game
#13rd October 2024
#Her link: https://appbrewery.github.io/python-day3-demo/
#ASCII Art: https://ascii.co.uk/art
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")

decision1 = input('''You're at a cross road. Where do you want to go?
      Type "left" or "right" ''').lower()

if decision1 == ("left"):
    decision2 = input('''You've come to a lake. There is an island in the middle of the lake.
                      Type "wait" to wait for a boat. Type "swim" to swim across.  ''').lower()
    if decision2 == ("wait"):
        decision3 = input('''You arrive at the island unharmed. There is a house with 3 doors.
      One red, one yellow and one blue. Which color do you choose? ''').lower()
        if decision3 == ("yellow"):
            print("You found the treasure! You win!")
        elif decision3 == ("red"):
            print("It's a room full of fire. Game Over!")
        elif decision3 == ("blue"):
            print("You enter a room of beasts. Game Over!")
        else:
            print("This room doesn't exist. Game Over!")
    else:
        print("Game Over! There was crocodiles in the water.")
else:
    print("Game Over! You fell into a hole.")

