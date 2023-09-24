#Простая задачка на декоратор property, выводим пронумерованный массив, поступающий на входных данных

class Notebook():
    
    def __init__(self, list):
        
        self._notes = list
    
    @property
    def notes_list(self):
        for id, item in enumerate(self._notes, start=1):
            print(f'{id}. {item}')

Console.ReadLine()    