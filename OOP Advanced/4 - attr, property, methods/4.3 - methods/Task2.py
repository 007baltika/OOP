

class User():
    
    def __init__(self, name):
        self.name = name
        self.friends = 0
        
    def add_friends(self, n):
        self.friends += n    
    

# TEST_1:
user = User('Arthur')

print(user.friends)
print()    
# TEST_2:
user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends)
print()    
# TEST_3:
user1 = User('Arthur')
user2 = User('Timur')

print(user1.friends)
print(user2.friends)

user1.add_friends(10)
user1.add_friends(20)

print(user1.friends)
print(user2.friends)
print()    
# TEST_4:
user = User('Arthur')

user.add_friends(0)
user.add_friends(1)
user.add_friends(2)
user.add_friends(0)
user.add_friends(1)
user.add_friends(2)

print(user.friends)    