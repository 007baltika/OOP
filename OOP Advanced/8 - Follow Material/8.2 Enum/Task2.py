# Реализуйте класс Seasons , описывающий перечисление с временами года.

# Перечисление должно иметь четыре элемента:
# • WINTER — элемент со значением 1
# • SPRING — элемент со значением 2
# • SUMMER — элемент со значением 3
# • FALL — элемент со значением 4

# Элемент перечисления должен иметь один метод:

# • text_value() — метод, принимающий в качестве аргумента код
# страны en или ru и возвращающий строковое значение элемента в
# зависимости от переданного аргумента. 

# Для WINTER en и ru значениями являются winter и зима соответственно, для SPRING — spring и весна , для SUMMER — summer и лето , для FALL — fall и осень

from enum import Enum

class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4
    
    def text_value(self, code):
        if code == 'ru': 
            if self.name == 'WINTER': return 'зима'
            if self.name == 'SPRING': return 'весна'
            if self.name == 'SUMMER': return 'лето'
            else: return 'осень'
        else: return self.name.lower() 
        


# INPUT DATA:

# TEST_1:
print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))
print()
# TEST_2:
for season in Seasons:
    print(season.text_value('en'), '->', season.text_value('ru'))
print()
# TEST_3:
for season in Seasons:
    print(season.name, season.value) 