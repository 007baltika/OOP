# Реализуйте класс NonNegativeInteger , описывающий дескриптор, который
# проверяет, что устанавливаемое или изменяемое значение атрибута является
# неотрицательным целым числом. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:
# • name — имя атрибута, за которым будет закреплен дескриптор
# • default — значение по умолчанию. Если не передан, имеет значение None

# При обращении к атрибуту дескриптор должен возвращать значение этого
# атрибута, если оно установлено. Если значение не установлено, должно
# возвращаться значение по умолчанию, указанное при создании дескриптора.

# Если значение по умолчанию равняется None , должно быть возбуждено
# исключение AttributeError с текстом: Атрибут не найден

# При установке или изменении значения атрибута дескриптор должен проверять,
# является ли это значение неотрицательным целым числом. Если значение не
# является неотрицательным целым числом, должно быть возбуждено
# исключение ValueError с текстом: Некорректное значение

class NonNegativeInteger:
    
    def __init__(self, name, default = None):
        self._attr = name
        self._default = default
        
    def __get__(self, obj, cls):
        try:
            if obj is None:
                return self
            else: return obj.__dict__[self._attr]
        except: 
            if self._default is None:
                raise AttributeError("Атрибут не найдет")
            else:
                return self._default    
        
    def __set__(self, obj, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            obj.__dict__[self._attr] = new_value
        else: 
            raise ValueError("Некорректное значение")
        
    def __delete__(self, obj):
        del obj.__dict__[self._attr]   
        
# TEST_1:
class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

print(student.score)
print()
# TEST_2:
class Student:
    score = NonNegativeInteger('score', 0)

student = Student()

print(student.score)
student.score = 0
print(student.score)
print()
# TEST_3:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)
print()
# TEST_4:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)
print()
# TEST_5:
class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

try:
    student.score = -90
except ValueError as e:
    print(e)
print()
# TEST_6:
class Student:
    score = NonNegativeInteger('score')

student = Student()

not_supported = [1.2, {1: 'one'}, {1, 2, 3}, [4, 5, 6], (7, 8, 9), '14']

for item in not_supported:
    try:
        student.score = item
    except ValueError as e:
        print(e)
print()
# TEST_7:
class Student:
    score = NonNegativeInteger('score')

print(Student.score.__class__)