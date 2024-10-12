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