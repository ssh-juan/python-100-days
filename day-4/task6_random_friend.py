# Challenge 2
#Who will pay the bill?
#Figure out how to pick a random name from the list of friends.
#Mix of Random + Lists
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Using the list (The way I did)
print("First way of doing")
rand = random.randint(0,4)
print(rand)
print(friends[rand])

#Doing directly on the list (Better way, she taught)
print("\n" + "Second way of doing")
print(random.choice(friends))