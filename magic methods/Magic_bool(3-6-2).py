#Вводим размеры сторон и что это за фигура (куб или прямоугольник)

class Quadrilateral():
    
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        if self.width == 0: self.width = self.height
        elif self.height == 0: self.height = self.width   
     
    def __str__(self):
        if self.width == self.height: 
            return f'Куб размером {self.width} * {self.height}'
        else: 
            return f'Прямоугольник размером {self.width} * {self.height}' 
        
    def __bool__(self):
        return self.width == self.height
    
Console.ReadLine()        