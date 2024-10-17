#Final Project Day 5 - Escaping the Maze - Reeborg's World
#16nd October 2024
#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#The way I solved. I did, not the best way but I was able to do it.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#there's a problem in this code

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else
        turn_left()