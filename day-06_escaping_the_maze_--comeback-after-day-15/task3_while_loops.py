#While Loops
#while something_is_true:
    #do something repeatedly

#Solving Hurdles again, but using WHILE
# Reeborg's Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

num_of_hurdles = 6

while num_of_hurdles > 0:
    jump()
    num_of_hurdles -= 1
    print(num_of_hurdles)