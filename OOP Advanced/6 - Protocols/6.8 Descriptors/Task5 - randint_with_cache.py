# Реализуйте класс RandomNumber , описывающий дескриптор, который при
# обращении к атрибуту возвращает случайное целое число в заданном диапазоне.
# При создании экземпляра класс должен принимать три аргумента в следующем
# порядке:
# • start — целое число
# • end — целое число
# • cache — булево значение, по умолчанию равняется false

# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и
# переменная, которой присваивается дескриптор.

# При обращении к атрибуту дескриптор должен возвращать случайное целое
# число от start до end включительно. Если в качестве значения
# параметра cache при создании дескриптора было указано значение true , при
# каждом обращении к атрибуту дескриптор должен возвращать то число, которое
# было сгенерировано при первом обращении.

# При установке или изменении значения атрибута дескриптор должен возбуждать
# исключение AttributeError с текстом:
# Изменение невозможно


import random

class RandomNumber:
    
    def __init__(self, start, end, cache = False):
        self._start = start
        self._end = end
        self._cache = cache
        
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._cache_int = random.randint(self._start, self._end)    
        
    def __get__(self, obj, cls):
        if self._cache == False:
            if obj is None:
                return self
            else:
                obj.__dict__[self._attr] = random.randint(self._start, self._end)
                return obj.__dict__[self._attr]
        else:
            if obj is None:
                return self
            else:
                obj.__dict__[self._attr] = self._cache_int
                return obj.__dict__[self._attr]      
        
    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")    
    
    def __delete__(self, obj):
        del obj.__dict__[self._attr]
   
   
        
# TEST_1:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])
print()
# TEST_2:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])
print()
# TEST_3:
class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)
print()
# TEST_4:
class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
print()
# TEST_5:
class MagicPoint:
    x = RandomNumber(20, 100, True)


magicpoint = MagicPoint()

value = magicpoint.x

for _ in range(20):
    print(magicpoint.x == value)
print()
# TEST_6:
class MagicPoint:
    x = RandomNumber(-1000, 1000)

magicpoint = MagicPoint()

for _ in range(50):
    print(magicpoint.x in range(-1000, 1001))
print()
# TEST_7:
class MagicPoint:
    x = RandomNumber(-1000, 1000)

    def __init__(self, x):
        self.x = x


try:
    magicpoint = MagicPoint(150)
except AttributeError as e:
    print(e)
print()
# TEST_8:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

print(MagicPoint.x.__class__)
print(MagicPoint.y.__class__)
print(MagicPoint.z.__class__)
                