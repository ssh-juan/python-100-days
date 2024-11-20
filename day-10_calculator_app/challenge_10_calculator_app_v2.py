#Final Project Day 10 - Calculator App
#19nd November 2024
#Her link: https://appbrewery.github.io/python-day10-demo

#Solution using her way of solving

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