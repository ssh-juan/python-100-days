#Inserted 'try' and 'except' to treat Value Error.
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number. Pleas try again with a numerical response such as '20'")
    age = int(input("How old are you? "))

#Inserted fstring
if age > 18:
    print(f"You can drive at age {age}")