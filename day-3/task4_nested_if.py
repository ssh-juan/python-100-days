#Using Nested IF to also check the age

print("Welcome to the Rollercoaster!")
height = int(input("What's your height in cm? "))

if height >= 120:
    print("You can ride the Rollercoaster! =)")
    age = int(input("What's your age? "))
    if age <= 18:
        print("You will pay $7")
    else:
        print("You will pay 12$")
else:
    print("Sorry, you have to grow taller before you can ride =(")