#Форматируем название города в правильную строку и проверяем что оканчивается на согласную

class City():
    
    def __init__(self, city):
        self.name = city.title()
        
    def __str__(self):
        return self.name
    
    def __bool__(self):
        return self.name[-1] not in 'aeiou' 



Console.ReadLine()                      
# a = City('new york')
# print(a.name)        