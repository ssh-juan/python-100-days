#Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies INSIDE function: {enemies}")

increase_enemies()
print(f"enemies OUTSIDE function: {enemies}")