#Random Module
#Doc: https://docs.python.org/3/library/random.html
import random

#Generating a random float
random_float_0_to_10 = random.random()
print(random_float_0_to_10)

#Generating a random float
random_float_0_to_10 = random.random() * 10
print(random_float_0_to_10)

#Generating a random float between 'a' and 'b'
random_float = random.uniform(1, 10)
print(random_float)