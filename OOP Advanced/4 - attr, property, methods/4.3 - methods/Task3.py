
class House:
    
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
        
    def paint(self, new_color):
        self.color = new_color
        return self.color
        
    def add_rooms(self, n):
        self.rooms += n
        return self.rooms        
    
 
# INPUT DATA:

# TEST_1:
house = House('white', 4)

print(house.color)
print(house.rooms)
print()   
# TEST_2:
house = House('white', 4)

house.paint('black')
house.add_rooms(1)

print(house.color)
print(house.rooms)
print()   
# TEST_3:
house1 = House('white', 4)
house2 = House('black', 3)

house1.paint('yellow')
house1.add_rooms(1)
house1.add_rooms(10)

print(house1.color, house1.rooms)
print(house2.color, house2.rooms)
print()   
# TEST_4:
house = House('white', 1)

house.paint('yellow')
house.paint('black')
house.add_rooms(0)
house.add_rooms(1)
house.add_rooms(3)
house.add_rooms(0)
house.add_rooms(1)

print(house.color)
print(house.rooms)    