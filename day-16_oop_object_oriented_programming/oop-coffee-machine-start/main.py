#Day 16 - OOP Coffee Machine Project
#04th December 2024

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    choice = input(f"What would you like? " + menu.get_items()).lower()
    if choice == "off":
        print("Turning machine off...")
        machine_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)