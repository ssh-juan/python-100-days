#Final Project Day 10 - Calculator App
#19nd November 2024
#Her link: https://appbrewery.github.io/python-day10-demo

#Solution following the steps of video, but it's still my solution
import art

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary
#print(operations["*"](8,4))

print(art.logo)

new_calc = True
while new_calc:
    n1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    operator = input("Pick an operation: ")
    n2 = float(input("What's the second number? "))

    result = operations[operator](n1,n2)

    print(f"{n1} {operator} {n2} = {result}")

    keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while keep_result in ("Y","y"):
        n1 = result
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        n2 = float(input("What's the second number? "))
        result = operations[operator](n1,n2)

        print(f"{n1} {operator} {n2} = {result}")

        keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")