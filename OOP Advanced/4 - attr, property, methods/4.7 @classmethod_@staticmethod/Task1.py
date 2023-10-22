# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент: radius — радиус круга

# Класс Circle должен иметь один метод класса:
# from_diameter() — метод, принимающий в качестве аргумента диаметр круга и возвращающий экземпляр класса Circle, созданный на основе переданного диаметра

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod    
    def from_diameter(cls, diameter):    
        radius = diameter / 2
        return cls(radius)
    
# TEST_1:
circle = Circle(5)

print(circle.radius)
print()
# TEST_2:
circle = Circle.from_diameter(10)

print(circle.radius)
print()
# TEST_3:
circle1 = Circle(51.5)
circle2 = Circle.from_diameter(45)

print(circle1.radius)
print(circle2.radius)
print()
# TEST_4:
array = [473, 474, 75, 182, 51, 491, 493, 494, 347, 305, 290, 381, 170, 355, 326, 97, 183, 120, 216, 475, 66, 306, 193, 257, 482, 200, 350, 236, 471, 468]

for diameter in array:
    circle = Circle.from_diameter(diameter)
    print(circle.radius)
print()
# TEST_5:
circle = Circle.from_diameter(120)
print(hasattr(circle, 'radius'))    