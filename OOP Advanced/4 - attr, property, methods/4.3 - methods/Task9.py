from math import sqrt

class Vector:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def abs(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
    
# INPUT DATA:

# TEST_1:
vector = Vector()

print(vector.x, vector.y)
print(vector.abs())
print()
# TEST_2:
vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())
print()
# TEST_3:
vector = Vector(18, 23)

print(vector.x, vector.y)
print(vector.abs())
print()
# TEST_4:
array = [(76, 164), (132, 195), (181, 97), (61, 124), (19, 158), (130, 116), (101, 191), (84, 35), (190, 21), (106, 49), (91, 192), (133, 155), (170, 24), (137, 107), (114, 142), (145, 170), (167, 148), (91, 43), (25, 15), (12, 20)]

for x, y in array:
    vector = Vector(x, y)
    print(vector.abs())    