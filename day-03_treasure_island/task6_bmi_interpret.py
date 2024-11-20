#BMI Calculator with Interpretations
#BMI < 18.5 = Underweight
#BMI >= 18.5 and < 25 = Normal Weight
#BMI >= 25 = Overweight

weight = int(input("What's your weight? "))
height = float(input("What's your height? "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}, you are Underweight")
elif bmi < 25:
    print(f"Your BMI is {round(bmi, 2)}, you are Normal Weight")
else: #>=25
    print(f"Your BMI is {round(bmi, 2)}, you are Overweight")