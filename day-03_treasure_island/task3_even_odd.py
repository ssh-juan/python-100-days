#Check Even or Odd
#Write some to check if the number in the input area is odd or even.
#If it's odd, print out the word "Odd" otherwise printout "Even"

num = int(input("Type a number: "))

#Checking the remainder
if num % 2 == 0:
    print(f"Number {num} is Even (par)")
else:
    print(f"Number {num} is Odd (ímpar)")