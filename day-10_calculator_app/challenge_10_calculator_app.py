#Final Project Day 10 - Calculator App
#19nd November 2024
#Her link: https://appbrewery.github.io/python-day10-demo
def add(n1,n2):
    return n1 + n2
def minus(n1,n2):
    return n1 - n2
def multiplier(n1,n2):
    return n1 * n2
def divisor(n1,n2):
    return n1 / n2

import art
print(art.logo)

new_operation = True
while new_operation:
    n1 = float(input("What's the first number? "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("What's the second number? "))

    if operation == "+":
        result_1 = add(n1,n2)
        print(f"{n1} {operation} {n2} = {result_1}")
    elif operation == "-":
        result_1 = minus(n1,n2)
        print(f"{n1} {operation} {n2} = {result_1}")
    elif operation == "*":
        result_1 = multiplier(n1,n2)
        print(f"{n1} {operation} {n2} = {result_1}")
    elif operation == "/":
        result_1 = divisor(n1,n2)
        print(f"{n1} {operation} {n2} = {result_1}")

    result_2 = None
    #Checking if will continue calculating with the result_1 or will do a new calculation
    keep_result = input(f"Type 'y' to continue calculating with {result_1}, or type 'n' to start a new calculation: ")
    if keep_result in ("Y","y"):
        while keep_result in ("Y","y"):
            operation = input("+\n-\n*\n/\nPick an operation: ")
            n2 = float(input("What's the second number? "))

            if result_2 is not None and result_2 != "":
                result_1 = result_2

            if operation == "+":
                result_2 = add(result_1,n2)
                print(f"{result_1} {operation} {n2} = {result_2}")
            elif operation == "-":
                result_2 = minus(result_1,n2)
                print(f"{result_1} {operation} {n2} = {result_2}")
            elif operation == "*":
                result_2 = multiplier(result_1,n2)
                print(f"{result_1} {operation} {n2} = {result_2}")
            elif operation == "/":
                result_2 = divisor(result_1,n2)
                print(f"{result_1} {operation} {n2} = {result_2}")

            keep_result = input(f"Type 'y' to continue calculating with {result_2}, or type 'n' to start a new calculation: ")