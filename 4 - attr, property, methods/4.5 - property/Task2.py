# Реализуйте класс HourClock , описывающий часы с одной лишь часовой стрелкой. 

# При создании экземпляра класс должен принимать один аргумент:
# • hours — количество часов. Если hours не является целым числом,
#   принадлежащим диапазону [1; 12] , должно быть
#   возбуждено исключение ValueError с текстом: Некорректное время


class HourClock:
    
    def __init__(self, hours):
        self.hours = hours
        
    def get_hours(self):
        return self._hours    
        
    def hours_setter(self, hours):
        if isinstance(hours, int) and hours in range(1, 13):
            self._hours = hours
        else: raise ValueError("Некорректное время")
        
    hours = property(fget = get_hours, fset=hours_setter)    
    
# INPUT DATA:

# TEST_1:
time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)
print()
# TEST_2:
time = HourClock(7)

try:
    time.hours = 15
except ValueError as e:
    print(e)
print()
# TEST_3:
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
print()
# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)
print()
# TEST_5:
try:
    HourClock('ten o`clock')
except ValueError as e:
    print(e)
print()
# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)
print()
# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, 'hours'))        
                