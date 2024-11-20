# Reeborg's Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Solving 1:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

for num in range(0,6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Solving 2 - BEST WAY:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(num):
    for exec in range(num):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

jump(6)