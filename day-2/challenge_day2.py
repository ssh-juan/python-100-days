#Final Project Day 2 - Tip Calculator
#12nd October 2024
#Her link: https://appbrewery.github.io/python-day2-demo/

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give: 10, 12 or 15 (percent)? $"))
people = int(input("How many people to spit the bill? "))

#calculating total bill + tip
total_value = total_bill * (1 + tip / 100)
value_per_person = total_value / people

print(f"The total is: ${round(total_value, 2)}")
print(f"Each person should pay: ${round(value_per_person, 2)}")
