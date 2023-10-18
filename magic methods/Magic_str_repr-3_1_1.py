#Проверяем входные данные на пол и выводим обращение
class Person:
    def __init__(self, name, surname, gender = 'male'):
         self.name = name
         self.surname = surname
         self.gender = gender
         
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, new_gender):
        if new_gender == 'male' or new_gender == 'female':
            self._gender = new_gender
        else: 
            self._gender = 'male'
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
        
    def __str__(self):
        if self._gender == 'male': return f'Гражданин {self.surname} {self.name}'
        elif self._gender == 'female': return f'Гражданка {self.surname} {self.name}'        
                 
Console.ReadLine()                 