

# Реализуйте класс декоратор @type_check , который принимает один аргумент:
# • types — список, элементами которого являются типы данных

# Декоратор должен проверять, что типы всех позиционных аргументов,
# передаваемых в декорируемую функцию, полностью сопоставляются с типами из
# списка types , то есть типом первого аргумента является первый элемент
# списка types , типом второго аргумента — второй элемент списка types , и так
# далее. 
# Если данное условие не выполняется, должно быть возбуждено исключение TypeError .

# Если количество позиционных аргументов больше, чем количество элементов в
# списке types , то не сопоставляемые аргументы не должны учитываться при
# проверке. Если количество позиционных аргументов меньше чем количество
# элементов в списке types , то не сопоставляемые типы из списка types не
# должны учитываться при проверке.


#КОНСТРУКЦИЯ, КОГДА КЛАСС(ДЕКОРАТОР) ПОЛУЧАЕТ АРГУМЕНТ, В ДАННОМ СЛУЧАЕ INT


import functools

class type_check:
    
    def __init__(self, types):
        self.types = types
        
    def __call__(self, func):   #ПЕРЕДАЧА ДЕКОРИРУЕМОЙ ФУНКЦИИ
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            
            len_value = min(len(self.types), len(args))
            
            def is_true():
                for i in range(0, len_value):
                    if type(args[i]) != self.types[i]:
                        return False
                return True
                    
            if is_true() == True:
                value = func(*args, **kwargs)
                return value
            else: raise TypeError
                    
        return wrapper
    

    
# INPUT DATA:

# TEST_1:
@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))
print()
# TEST_2:
@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))
print()
# TEST_3:
@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print()
# TEST_4:
@type_check([int, int])
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3.0))
print()
# TEST_5:
@type_check([])
def add(a, b):
    return a + b


print(add(1, 2))
print()
# TEST_6:
@type_check([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))    