#Программа создает роботов и удаляет или создает их при вызове методов 

class Robot():
    
    population = 0
    
    
    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {self.name} был создан')
        
    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')
        
    def say_hello(self):
        return f'Робот {self.name} приветствует тебя, особь человеческого рода'
    
    @classmethod
    def how_many(Robot):
        return f'{Robot.population}, вот сколько нас еще осталось'    
    
Console.ReadLine() 