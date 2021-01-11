class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.follwing = 0

    def follow(self, user):
        user.followers += 1
        self.follwing += 1

user_1 = User()
user_1.id = '001'

user_2 = User()

