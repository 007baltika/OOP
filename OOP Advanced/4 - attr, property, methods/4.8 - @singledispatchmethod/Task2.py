# Реализуйте класс Negator . При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Negator должен иметь один статический метод:
# • neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. 

# Если методу передаетсяцелое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. 
# Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. 
# Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом: 'Аргумент переданного типа не поддерживается'

from functools import singledispatchmethod

class Negator:
    
    @singledispatchmethod
    @staticmethod
    def neg(object):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def object_is_int(object):
        return -object
    
    @neg.register(bool)
    @staticmethod
    def object_is_bool(object):
        object = not object
        return object
    
# INPUT DATA:

# TEST_1:
print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
print()
# TEST_2:
try:
    Negator.neg('number')
except TypeError as e:
    print(e)
print()
# TEST_3:
not_supported = [[1, 2, 3], (4, 5, 6), {1: 'one'}, {10, 11, 12}, 'Timothy John «Tim» Berners-Lee']

for item in not_supported:
    try:
        Negator.neg(item)
    except TypeError as e:
        print(e)    
    