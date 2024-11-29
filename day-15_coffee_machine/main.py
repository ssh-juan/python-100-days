#Day 15 - Coffee Machine Project
#29th November 2024

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
if choice == "report":
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    #print(money??)
elif choice in ("espresso", "latte", "cappuccino"):
    print("Please insert coins.")
    quarters = input("How many quarters (25¢)?: ")
    dimes = input("How many dimes (10¢)?: ")
    nickles = input("How many nickles (5¢)?: ")
    pennies = input("How many pennies (1¢)?: ")

    def validate_coins(quarters, dimes, nickles, pennies):
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
elif choice == "off":
    print("Turning machine off.")
else:
    print("You inserted an invalid input. Type again.")