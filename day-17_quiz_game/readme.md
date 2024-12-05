# Day 17 - 04th December 2024
Creating Classes

## Lessons Learned
- Class
    - A blueprint
    - Should be PascalCase
```py
#Syntax
class User:     #Blueprint
    pass

user_1 = User() #Object
```
- Attributes
    - What the object <u>**has**</u>
    - An attribute is a variable associated to an object
```py
class User:
    pass

user_1 = User()

#Adding attributes
#An attribute is a variable associated to an object
user_1.id = "001"
user_1.username = "Juan"
print(user_1.username)
```
- Constructor
    - A part of blueprint that specifies what should happen when our object is being constructed, it's basically initializing an object.
```py
class Car:
    def __init__(self):
        #initialize attributes
```
- Methods
    - What the object <u>**does**</u>
    - A function
```py
#race mode has 2 seats, instead of 5
class Car:
    def enter_race_mode():
        self.seats = 2
```

## Final Project
Quiz Game