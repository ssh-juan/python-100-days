#Modifying variables with Global Scope
#AVOID DOING THIS

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies INSIDE function: {enemies}")

increase_enemies()
print(f"enemies OUTSIDE function: {enemies}")


#Another way of doing without using global
enemies = 1

def increase_enemies(enemy):
    print(f"enemies INSIDE function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies OUTSIDE function: {enemies}")