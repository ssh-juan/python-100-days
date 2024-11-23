#Local Scope
#Exists within functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

#Line below causes an error, because the variable is 'not defined'. It does not exists outside the function
#print(potion_strength) 