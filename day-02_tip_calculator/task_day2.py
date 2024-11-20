# Day 2

# Python Primitive Data Types
#1. Strings
#2. Integers
#3. Floats
#4. Booleans

# Subscripting - pulling out a particular element from a string
print("Hello"[0])   # =H
print("Hello"[-1])  # =o

# String - concatenating
print("123" + "345")

# Integer
print(123 + 345)

# Large Integers
print(123456789)
# We can use the underline (_) to turn it better human readable
print(123_456_789)

# Float = Floating Point Number
pi = 3.14159
print(pi)

# Boolean
# Always begins with CAPITAL LETTERS
print(True)
print(False)

#function: type()
print(type("String"))
print(type(123))
print(type(pi))
print(type(True))

# Converting into a number
#function: int()
int("123")
print("123" + "456")            #not converted
print(int("123") + int("456"))  #converted

#there's also functions to convert such as:
#float()
#str()
#bool()

#Challenge: Make this line run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))

############################################################################

#Mathematical Operations in Python
print("My age: " + str(23))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) #When dividing, you always get a float
print(type(6 / 3))

print("\n")

print(5 / 3)
print(5 // 3) #When using double slashes (//) to divide, the function wipes out all the rest of numbers
print(type(5 // 3))

print("\n")

print("Potenciação")
print(2 ** 2) #power uses double asterisk (**)

# PEMDASLR - Ordem of Execution
# Parentheses ()
# Exponents **
# Multiplication * | Division /
# Addition + | Subtraction -
# Left to Right

#What will be the output of the following calcule?
#(3 * 3 + 3 / 3 - 3)
print(3 * 3 + 3 / 3 - 3) # =7

#Change the code so it outputs 3
#(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#Number Manipulation - How to round number
#function: round(number, ndigits)
bmi = 24.151672503320853
print("Your BMI is: " + str(round(bmi, 3)))
print("Your BMI is: " + str(round(bmi)))

#Score
score = 0

#User scores a point
score += 1
print (score)

print("Your score is " + str(score))

#To not need to convert all the variables to string, we can use f-Strings
#syntax: print(f"My name is {name}")
#The 'f' needs to be between the first parentheses and the first quote
#The variables should be between {}
score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")