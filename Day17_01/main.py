class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.followers = 0 
        self.following = 0

    def follow(self, user):
        user.followers+=1
        self.following+=1

user1=User("001", "Vibin")
user2=User("002", "Febin")
print(f"{user1.id} with {user1.name} created with {user1.followers} followers ")
print(f"{user2.id} with {user2.name} created with {user2.followers} followers")

user1.follow(user2)
print(f"{user1.id} with {user1.name} created with {user1.followers} followers and follows {user1.following} users")
print(f"{user2.id} with {user2.name} created with {user2.followers} followers and follows {user2.following} users")