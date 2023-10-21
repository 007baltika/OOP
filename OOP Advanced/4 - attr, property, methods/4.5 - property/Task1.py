# Реализуйте класс Rectangle , описывающий прямоугольник. 
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# • length — длина прямоугольника
# • width — ширина прямоугольника

# Класс Rectangle должен иметь два свойства:
# • perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
# • area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

# Примечание 1 При изменении сторон прямоугольника должны изменяться его периметр и площадь.

class Rectangle:
    
    def __init__(self, length, width):
        
        self.length = length
        self.width = width
        
    def get_perimeter(self):
        return (self.length + self.width) * 2   
    
    def get_area(self):
        return self.length * self.width 
        
    perimeter = property(get_perimeter)    
    area = property(get_area)    
    
# TEST_1:
rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
print()
# TEST_2:
rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
print()

# TEST_3:
rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')    