# Реализуйте класс Formatter . При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Formatter должен иметь один статический метод:
# • format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict 
# и выводящий информацию о переданном объекте в формате, зависящем от его типа. 

# Если переданныйобъект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом: 'Аргумент переданного типа не поддерживается'


from functools import singledispatchmethod

class Formatter:
    
    @singledispatchmethod
    @staticmethod
    def format(object):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @staticmethod
    def object_is_int(object):
        print(f'Целое число: {object}')
    
    @format.register(float)
    @staticmethod
    def object_is_float(object):
        print(f'Вещественное число: {object}')
    
    @format.register(tuple)
    @staticmethod
    def object_is_tuple(object):
        print(f'Элементы кортежа: {", " .join([str(a) for a in object])}')
    
    @format.register(list)
    @staticmethod
    def object_is_list(object):
        print(f'Элементы списка: {", " .join([str(a) for a in object])}')
    
    @format.register(dict)
    @staticmethod
    def object_is_dict(object):
        print(f'Пары словаря: {", ".join([str(tup) for tup in [a for a in object.items()]])}')
    

# TEST_1:
Formatter.format(1337)
Formatter.format(20.77)
print()
# TEST_2:
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
print()
# TEST_3:
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
print()
# TEST_4:
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
print()
# TEST_5:
not_supported = [str, type, bool, dict, tuple, list]

for item in not_supported:
    try:
        Formatter.format(item)
    except TypeError as e:
        print(e)    
    