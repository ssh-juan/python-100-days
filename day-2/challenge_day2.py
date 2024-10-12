#Final Project Day 2 - Tip Calculator
#12nd October 2024
#Her link: https://appbrewery.github.io/python-day2-demo/

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give: 10%, 12% or 15%? $")
people = input("How many people to spit the bill? ")

#turning tip from integer to percentage
tip_percentage = int(tip) / int(100)
tip_calculated = float(total_bill) * float(tip_percentage)

total_value = float(total_bill) + float(tip_calculated)
value_per_person = float(total_value) / int(people)

print(f"The total is: ${total_value}")
print(f"Each person should pay: ${round(value_per_person, 2)}")
