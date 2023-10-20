from math import pi, sqrt
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self.area = pi * pow(radius, 2)
        self.diameter = sqrt(self.area * 4 / pi)
       
# INPUT DATA:

# TEST_1:
circle = Circle(1)

print(circle.radius)
print() 
# TEST_2:
circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)
print() 
# TEST_3:
circle = Circle(20)
print(hasattr(circle, 'radius'))
print(hasattr(circle, 'diameter'))
print(hasattr(circle, 'area'))
print() 
# TEST_4:
array = [85, 74, 34, 33, 19, 15, 65, 91, 17, 15, 95, 17, 57, 35, 61, 29, 98, 74, 65, 27]

for radius in array:
    circle = Circle(radius)
    print('Радиус =', circle.radius, 'Диаметр =', circle.diameter, 'Площадь =', round(circle.area, 2))        