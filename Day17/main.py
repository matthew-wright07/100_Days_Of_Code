class User:
    def __init__ (self, user_id):
        self.id = user_id

user_1 = User("1")

def makeUser(user_id):
    return {
        id:user_id,
        }

user2 = makeUser("2")