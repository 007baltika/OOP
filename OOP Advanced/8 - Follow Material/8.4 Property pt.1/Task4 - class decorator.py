

# Реализуйте класс декоратор @returns , который принимает один аргумент:
# • datatype — тип данных

# Декоратор должен проверять, что возвращаемое значение декорируемой
# функции принадлежит типу datatype . Если возвращаемое значение
# принадлежит какому-либо другому типу, должно быть возбуждено
# исключение TypeError 


#КОНСТРУКЦИЯ, КОГДА КЛАСС(ДЕКОРАТОР) ПОЛУЧАЕТ АРГУМЕНТ, В ДАННОМ СЛУЧАЕ INT


import functools

class returns:
    
    def __init__(self, datatype):
        self.datatype = datatype
        
    def __call__(self, func):   #ПЕРЕДАЧА ДЕКОРИРУЕМОЙ ФУНКЦИИ
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)  # ВЫЗОВ ДЕКОРИРУЕМОЙ ФУНКЦИИ
            if isinstance(value, self.datatype):
                return value
            else: raise TypeError
        return wrapper
    

# INPUT DATA:

# TEST_1:
@returns(int)
def add(a, b):
    return a + b

print(add(1, 2))
print()
# TEST_2:
@returns(int)
def add(a, b):
    return a + b

try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))
print()
# TEST_3:
@returns(list)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))
print()
# TEST_4:
@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))
print()
# TEST_5:
@returns(tuple)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2, 3], [4, 5, 6]))
except TypeError as e:
    print(type(e))
print()
# TEST_6:
@returns(int)
def add(a, b):
    return a + b

print(add(a=10, b=5))   