#Challenge 1
#Create a coin flip program. 
#It should randomly print "Heads" or "Tails" every time it is run.
import random

random = random.randint(0, 1)
print(random)

if random == 0:
    print("Heads")
else:
    print("Tails")