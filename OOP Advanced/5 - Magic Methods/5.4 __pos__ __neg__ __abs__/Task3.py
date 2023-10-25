
from math import sqrt
class Vector:
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))  
    
# TEST_1:
vector = Vector(3, -4)

print(+vector)
print(-vector)
print(abs(vector))
print()
# TEST_2:
vector = Vector(-8, -6)

print(+vector)
print(-vector)
print(abs(vector))
print(repr(vector))
print()
# TEST_3:
vectors = [(92, -73), (-3, -29), (-95, 22), (62, -55), (80, 59), (58, 75), (7, -76), (32, -68), (-9, 58), (11, 51),
           (22, -73), (54, 47), (-58, -79), (-46, 56), (80, 84), (41, 16), (-29, 78), (80, -94), (-46, -86), (-43, -76),
           (82, -43), (-67, -30), (-57, -53), (85, -91), (-39, 55), (-65, 25), (-54, 51), (-11, 22), (-47, 7),
           (-12, -75), (-5, -63), (31, -43), (-69, 6), (89, 47), (60, -63), (-96, -33), (-65, 49), (-98, 95), (96, 44),
           (-87, 1), (-89, -61), (-11, -29), (-57, 20), (87, 40), (15, -64), (-10, -43), (-29, 58), (98, -10), (0, 55),
           (85, 25), (42, -79), (-1, -13), (5, 77), (6, -24), (-93, 19), (-54, 21), (-6, 8), (-50, -49), (-22, -87),
           (-29, 100), (0, 0), (-81, 20), (-47, -35), (100, 90), (-83, 80), (52, 62), (-72, -18), (14, 21), (25, 55),
           (55, -71), (79, -11), (22, -82), (46, -18), (36, 66), (23, 41), (81, 19), (67, 26), (-81, 85), (19, 43),
           (39, 77), (3, 9), (-41, 8), (6, 1), (-98, -27), (33, -64), (45, -68), (58, -93), (67, -73), (-76, 0),
           (-25, 50), (-56, -40), (92, -56), (74, -27), (57, -96), (-11, 25), (-17, -9), (-42, 67), (-76, 80),
           (-68, -34), (-73, -17), (-23, -76)]

for x, y in vectors:
    vector = Vector(x, y)
    print('{}; {}; {}'.format(+vector, -vector, abs(vector)))
print()
# TEST_4:
coordinates = [(-2, -12), (-78, -22), (-90, 58), (10, -37), (25, 60)]
vectors = [Vector(x, y) for x, y in coordinates]
print(vectors)          