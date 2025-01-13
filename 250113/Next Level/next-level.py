user2_id, user2_level = input().split()
user2_level = int(user2_level)

class game:
    def __init__(self, user2_id = "codetree", user2_level = "10"):
        self.user2_id = user2_id
        self.user2_level = user2_level

user1 = game()
print("user", user1.user2_id, "lv", user1.user2_level)
user2 = game(user2_id, user2_level)
print("user", user2.user2_id, "lv", user2.user2_level)
