##Using IF and ELSE IF
#<=12 = $5
#13-18 = $7
#>=19 = $12

print("Welcome to the Rollercoaster!")
height = int(input("What's your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the Rollercoaster! =)")
    age = int(input("What's your age? "))
    if age <= 12:
        print("Child tickets are $5")
        bill = 5
    elif age <=18:
        print("Youth tickets are 7$")
        bill = 7
    else: #>=19
        print("Adult tickets are $12")
        bill = 12
    
    wants_photo = input("Do you want to have a photo take? Type 'Y' for Yes or 'N' for No ")
    if wants_photo in("Y","y"):
        #Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride =(")