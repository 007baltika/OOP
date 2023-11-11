# Реализуйте класс TypeChecked , описывающий дескриптор, который проверяет,
# что устанавливаемое или изменяемое значение атрибута принадлежит
# определенному типу данных. При создании экземпляра класс должен принимать
# произвольное количество позиционных аргументов, каждый из которых является типом данных.

# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и
# переменная, которой присваивается дескриптор.

# При обращении к атрибуту дескриптор должен возвращать значение этого
# атрибута, если оно установлено. Если значение атрибута не установлено, должно
# быть возбуждено исключение AttributeError с текстом: Атрибут не найден

# При установке или изменении значения атрибута дескриптор должен проверять,
# принадлежит ли это значение одному из типов, указанных при создании
# дескриптора. Если значение не принадлежит ни одному из типов, должно быть
# возбуждено исключение TypeError с текстом: Некорректное значение

class TypeChecked:
    
    def __init__(self, *args):
        self.types = args
    
    def __set_name__(self, cls, attr):
        self._attr = attr
        
    def __get__(self, obj, cls):
        
        try:
            if obj is None:
                return self
            else: return obj.__dict__[self._attr]
        except: raise AttributeError("Атрибут не найден") 
        
    def __set__(self, obj, value):
        if type(value) in self.types:
            obj.__dict__[self._attr] = value
        else: raise TypeError("Некорректное значение")
        
    def __delete__(self, obj):
        del obj.__dict__[self._attr]     
        

# TEST_1:
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

print(student.name)
print()
# TEST_2:
class Student:
    name = TypeChecked(str)

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
print()
# TEST_3:
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)
print()
# TEST_4:
class Student:
    age = TypeChecked(int, float)

student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)
print()
# TEST_5:
class Vector:
    x = TypeChecked(float)
    y = TypeChecked(float)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

pairs = [('12', '89'), ([1, 2], [3, 4]), ({1: 2}, {3: 4}), (True, False), (1.2, 3.4)]

for x, y in pairs:
    try:
        vector = Vector(x, y)
        print(vector)
    except TypeError as e:
        print(e)
print()
# TEST_6:
class Student:
    name = TypeChecked(str)

print(Student.name.__class__)