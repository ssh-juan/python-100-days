year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

#The error is that the conditions are missing year 1994, so it never has return.

#FIXED: Changed the elif condition to greater than or EQUAL TO '>='