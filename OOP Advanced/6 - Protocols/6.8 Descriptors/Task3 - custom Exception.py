# Реализуйте класс LimitedTakes , описывающий дескриптор, который позволяет
# получать значение атрибута лишь определенное количество раз. При создании
# экземпляра класс должен принимать один аргумент:
# • times — количество доступных обращений к атрибуту

# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и
# переменная, которой присваивается дескриптор.

# При обращении к атрибуту дескриптор должен возвращать значение этого
# атрибута, если оно установлено. Если значение атрибута не установлено, должно
# быть возбуждено исключение AttributeError с текстом: Атрибут не найден

# Если к атрибуту было выполнено times обращений, во время всех последующих
# обращений должно возбуждаться исключение MaxCallsException с текстом: Превышено количество доступных обращений

class MaxCallsException(Exception):
    pass

class LimitedTakes:
    
    def __init__(self, times):
        self._times = times
        self.count = 0
        
    def __set_name__(self, cls, attr):
        self._attr = attr    
    
    def __get__(self, obj, cls):
        if self.count < self._times:
            try:
                self.count += 1
                if obj is None:
                    return self
                else: return obj.__dict__[self._attr]
            except: raise AttributeError("Атрибут не найден")
        else: raise MaxCallsException("Превышено количество доступных обращений")          
        
    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
        
    def __delete__(self, obj):
        del obj.__dict__[self._attr]          
        
  
  
        
# TEST_1:
class Student:
    name = LimitedTakes(3)

student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)
print()
# TEST_2:
class Student:
    name = LimitedTakes(3)

student = Student()

for _ in range(100):
    student.name = 'Gwen'
    
print(student.name)
print()
# TEST_3:
class Programmer:
    name = LimitedTakes(1)


programmer = Programmer()

try:
    print(programmer.name)
except AttributeError as e:
    print(e)
print()
# TEST_4:
class Programmer:
    name = LimitedTakes(1000)


programmer = Programmer()
programmer.name = 'Gvido'

for _ in range(1000):
    programmer.name

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)
print()
# TEST_5:
class Student:
    name = LimitedTakes(3)


class Programmer:
    name = LimitedTakes(1)


student = Student()
programmer = Programmer()

student.name = 'Gwen'
programmer.name = 'Mantrida'

for _ in range(3):
    print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)


print(programmer.name)

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)
print()
# TEST_6:
class Student:
    first_name = LimitedTakes(3)
    last_name = LimitedTakes(1)


student = Student()

student.first_name = 'Gwen'
student.last_name = 'Stacy'


for _ in range(3):
    print(student.first_name)

try:
    print(student.first_name)
except MaxCallsException as e:
    print(e)

print(student.last_name)
try:
    print(student.last_name)
except MaxCallsException as e:
    print(e)
print()
# TEST_7:
class Student:
    name = LimitedTakes(3)

print(Student.name.__class__)
       