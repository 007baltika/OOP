


# сравнение 2х классов только по x и y

# quadrant - расположение точки в координатной четверти

# symmetric x - относительно оси x, symmetric y - относительно оси y. Функция должна возвращать новый экземпляр класса Point


from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, compare=False)
    
    def symmetric_x(self):
        return Point(self.x, -self.y)
    
    def symmetric_y(self):
        return Point(-self.x, self.y)
    
    
    def __post_init__(self):
        if self.x > 0 and self.y > 0: self.quadrant = 1
        elif self.x < 0 and self.y > 0: self.quadrant = 2
        elif self.x < 0 and self.y < 0: self.quadrant = 3
        elif self.x > 0 and self.y < 0: self.quadrant = 4
        elif self.x == 0.0 or self.y == 0.0: self.quadrant = 0
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, quadrant={self.quadrant})'  
    
# INPUT DATA:

# TEST_1:
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)
print()
# TEST_2:
point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
print()
# TEST_3:
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)
print()
# TEST_4:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point)
print()
# TEST_5:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_x())
print()
# TEST_6:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_y())
        