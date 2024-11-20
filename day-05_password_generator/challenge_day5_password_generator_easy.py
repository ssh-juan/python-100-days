#Final Project Day 5 - Password Generator
#15nd October 2024
#Her link: https://appbrewery.github.io/python-day5-demo

#Easy level
#Generates the password in sequence: letters, then symbols, then numbers.

import random
import string

print("Welcome to Juan's PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for letter in range(nr_letters):
    password += random.choice(string.ascii_letters)

for symbol in range(nr_symbols):
    password += random.choice(string.punctuation)

for num in range(nr_numbers):
    password += str(random.randint(0,9))

print(f"The password is: {password}")