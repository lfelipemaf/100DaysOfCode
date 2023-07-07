class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.following = 0

    def follower(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Felipe")
user_2 = User("002", "Luiz")

print(f"{user_1.username}\nFollowers:{user_1.followers} Following:{user_1.following}")
print(f"{user_2.username}\nFollowers:{user_2.followers} Following:{user_2.following}")
print("------")

user_1.follower(user_2)
print(f"{user_1.username}\nFollowers:{user_1.followers} Following:{user_1.following}")
print(f"{user_2.username}\nFollowers:{user_2.followers} Following:{user_2.following}")
print("------")

user_2.follower(user_1)
print(f"{user_1.username}\nFollowers:{user_1.followers} Following:{user_1.following}")
print(f"{user_2.username}\nFollowers:{user_2.followers} Following:{user_2.following}")