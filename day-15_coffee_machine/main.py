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

def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    #if money not none and > 0
        #print(money??)

def check_resources(choice):
    """Check if there is enough resources the produce the drink."""
    if choice == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            return 0
        else:
            return 1
    elif choice == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            return 0
        else:
            return 1
    elif choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return 0
        else:
            return 1

def validate_coins():
    """Validates if the amount of coins is enough to buy the drink."""
    print("Please insert coins.")
    global change

    quarters = int(input("How many quarters (25¢)?: "))
    dimes = int(input("How many dimes (10¢)?: "))
    nickles = int(input("How many nickles (5¢)?: "))
    pennies = int(input("How many pennies (1¢)?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if total >= MENU[choice]["cost"]:
        if total == MENU[choice]["cost"]:
            return 0
        else:
            change = total - MENU[choice]["cost"]
            return change
    else:
        return 999

def deduct_resources(choice):
    if choice == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        return resources
    elif choice == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        return resources
    else: #espresso
        resources["water"] -= 50
        resources["coffee"] -= 18
        return resources

change = 0
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == "report":
        print_report()
    elif choice in ("espresso", "latte", "cappuccino"):
        if check_resources(choice) == 0:
            if validate_coins() != 999:
                deduct_resources(choice)
                if change > 0:
                    print(f"Here is your ${round(change,2)} in change.")
                    change = 0
                print(f"Here is your {choice}☕. Enjoy! =)")
        else:
            print(f"There is not enough resources to make {choice}.")
    elif choice == "off":
        print("Turning machine off.")
        machine_on = False
    else:
        print("You inserted an invalid input. Type again.")