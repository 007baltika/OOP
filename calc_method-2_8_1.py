#Простая задача на property - вывод площадки прямоугольника

class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @property    
    def area(self):
        return self.length * self.width
    
Console.ReadLine()  
        