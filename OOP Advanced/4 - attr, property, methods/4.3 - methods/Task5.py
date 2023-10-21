

class Bee:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def move_up(self, n):
        self.y += n   
    
    def move_down(self, n):
        self.y -= n  
    
    def move_right(self, n):
        self.x += n  
    
    def move_left(self, n):
        self.x -= n   
    
# INPUT DATA:

# TEST_1:
bee = Bee()

print(bee.x, bee.y)
print()
# TEST_2:
bee = Bee()

bee.move_up(1)
bee.move_right(1)
bee.move_down(1)
bee.move_left(1)

print(bee.x, bee.y)
print()
# TEST_3:
bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)
print()
# TEST_4:
bee = Bee(3, 4)
print(bee.x, bee.y)

bee.move_right(3)
print(bee.x, bee.y)

bee.move_up(5)
print(bee.x, bee.y)

bee.move_left(2)
print(bee.x, bee.y)

bee.move_down(10)
print(bee.x, bee.y)    
    