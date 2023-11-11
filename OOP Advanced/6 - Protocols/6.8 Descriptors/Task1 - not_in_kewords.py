
# Реализуйте класс NonKeyword , описывающий дескриптор, который проверяет,
# что устанавливаемое или изменяемое значение атрибута не является строковым
# ключевым словом в Python. При создании экземпляра класс должен принимать
# один аргумент:
# • name — имя атрибута, за которым будет закреплен дескриптор

# При обращении к атрибуту дескриптор должен возвращать значение этого
# атрибута, если оно установлено. Если значение атрибута не установлено, должно
# быть возбуждено исключение AttributeError с текстом:
# Атрибут не найден

# При установке или изменении значения атрибута дескриптор должен проверять,
# не является ли это значение строковым ключевым словом в Python. Если
# значение является строковым ключевым словом, должно быть возбуждено
# исключение ValueError с текстом:
# Некорректное значение

import keyword

class NonKeyword:
    
    def __init__(self, attr):
        self._attr = attr
        
    def __get__(self, obj, cls):
        try:
            if obj is None:
                return self
            else: 
                return obj.__dict__[self._attr]
        except: raise AttributeError("Атрибут не найден")
    
    def __set__(self, obj, new_value):
        if new_value not in keyword.kwlist:
            obj.__dict__[self._attr] = new_value
        else: raise ValueError("Некорректное значение")
        
    def __delete__(self, obj):
        del obj.__dict__[self._attr]    
    

# TEST_1:
class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)
print()
# TEST_2:
class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
print()
# TEST_3:
class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)
print()
# TEST_4:
class Student:
    name = NonKeyword('name')

student = Student()

try:
    student.name = 'class'
except ValueError as e:
    print(e)
print()
# TEST_5:
from keyword import kwlist

class Student:
    name = NonKeyword('name')

student = Student()

for kw in kwlist:
    try:
        student.name = kw
    except ValueError as e:
        print(e)
print()
# TEST_6:
class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)
print()
# TEST_7:
class Student:
    name = NonKeyword('name')

print(Student.name.__class__)