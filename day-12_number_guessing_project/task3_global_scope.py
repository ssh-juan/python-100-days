#Global Scope
#Variables can be accessible outside the function

#The difference between Local and Global Scope is where you define the variables.

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion() #It is able to print 'player_health' because it was already defined outside the function.