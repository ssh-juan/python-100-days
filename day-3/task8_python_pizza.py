#Python Pizza Delivery
'''
Based on a user's order, work out their final bill.
Use the input() to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
Small Pizza (S): $15
Medium Pizza (M): $20
Large Pizza (L): $25

Add Pepperoni for Small Pizza: +$2
Add Pepperoni for Medium or Large Pizza: +$3
Add extra cheese for any size Pizza: +$1
'''

print("Welcome to Juan's Python Pizza Deliveries! =)")
size = input("What size pizza do you want: S, M or L? ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
#Checking Size
if size in("S","s"):
    bill = 15
elif size in("M","m"):
    bill = 20
elif size in("L","l"):
    bill = 25
else:
    print("You typed the wrong inputs ;-;")

#Checking if Pepperoni
if pepperoni in("Y","y"):
    if size in("S","s"):
        bill += 2
    elif size in("M","m","L","l"):
        bill += 3

#Checking if Extra Cheese
if extra_cheese in("Y","y"):
    bill += 1

if bill > 0:
    print(f"Your final bill is: ${bill}.")