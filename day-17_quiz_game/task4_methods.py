#Methods
#Adding 'Methods' to a 'Class'

#Example: following someone on Instagram

class User():
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Juan")
user_2 = User("002","Josh")

user_1.follow(user_2)
print(f"User 1 - Followers: {user_1.followers}")
print(f"User 1 - Following: {user_1.following}")
print("\n")
print(f"User 2 - Followers: {user_2.followers}")
print(f"User 2 - Following: {user_2.following}")