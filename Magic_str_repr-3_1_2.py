#Программа получает произвольное число аргументов и выводит упорядоченный массив в формате (массив)

class Vector():
    
    def __init__(self, *kwargs):
        self.values = []
        for value in kwargs:
            if isinstance(value, int):
                self.values.append(value)
    
    def __str__(self):
        if len(self.values) > 0: 
            self.values.sort()
            mass_nums_as_str = []
            for i in range(0, len(self.values)):
                mass_nums_as_str.append(str(self.values[i]))
                
            return f'Вектор({", ".join(mass_nums_as_str)})'    
        else: return "Пустой вектор"  


v1 = Vector(1,5,1)
print(v1) #Вектор(1, 1, 5)       
v2 = Vector()
print(v2) #Пустой вектор  
     
#Console.ReadLine()                      