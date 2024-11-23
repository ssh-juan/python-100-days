#Nesting

#The difference between Local and Global Scope is where you define the variables.

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

#Now this line is an error, because it is only defined inside the function 'game()'.
#drink_potion()