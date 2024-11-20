#Using IF and ELSE IF
#<=12 = $5
#13-18 = $7
#>=19 = $12

print("Welcome to the Rollercoaster!")
height = int(input("What's your height in cm? "))

if height >= 120:
    print("You can ride the Rollercoaster! =)")
    age = int(input("What's your age? "))
    if age <= 12:
        print("You will pay $5")
    elif age <=18:
        print("You will pay 7$")
    else: #>=19
        print("You will pay $12")
else:
    print("Sorry, you have to grow taller before you can ride =(")