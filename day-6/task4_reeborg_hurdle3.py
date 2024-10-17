# Reeborg's Hurdle 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Solving:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

#or while at_goal() != True:​
while not at_goal():
    jump()


# ######## Code below didn't work, but was a good try
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()

# def go_down():
#     turn_right()
#     move()
#     turn_left()

# num = 2    

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front() and num % 2 == 0:
#         jump()
#         num += 1
#     elif wall_in_front() and num % 2 != 0:
#         go_down()
#         num += 1
        