#Calculate the BMI using weight and height
height = 1.82
weight = 80

print("Height is: " + str(height))
print("Weight is: " + str(weight))

bmi = weight / height ** 2

print("Your BMI is: " + str(bmi))

#Number Manipulation - How to round number
#function: round(number, ndigits)
print("Your BMI is: " + str(round(bmi, 2)))
print("Your BMI is: " + str(round(bmi)))