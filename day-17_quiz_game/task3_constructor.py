#Constructor
#Initializing an object
#Special function: __init__

class Car:
    def __init__(self, seats):
        print("exec...")
        self.seats = seats

my_car = Car(5)
print(my_car.seats) #seats = 5

class User():
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0

user_1 = User("001","Juan")
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("002","Josh")
print(user_2.id)
print(user_2.username)
print(user_2.followers)