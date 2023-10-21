from math import pi

class Circle:
    
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * pow(radius, 2)
        
    def get_radius(self):
        return self._radius
    
    def get_diameter(self):
        return self._diameter    
    
    def get_area(self):
        return self._area  
    
# INPUT DATA:

# TEST_1:
circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
print()
# TEST_2:
circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
print()
# TEST_3:
circle = Circle(50)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
print()
# TEST_4:
circle = Circle(18.32)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
print()
# TEST_5:
circle = Circle(0.7)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
print()
# TEST_6:
circle = Circle(10)
print(hasattr(circle, '_radius'))
print(hasattr(circle, '_diameter'))
print(hasattr(circle, '_area'))    