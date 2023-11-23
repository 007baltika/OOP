
# Реализуйте класс декоратор @takes_numbers , который проверяет, что все
# аргументы, передаваемые в декорируемую функцию, принадлежат
# типам int или float . Если хотя бы один аргумент принадлежит какому-либо
# другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргументы должны принадлежать типам int или float

# Примечание: Не забывайте, что декоратор не должен поглощать возвращаемое
# значение декорируемой функции, а также должен уметь декорировать функции с
# произвольным количеством позиционных и именованных аргументов.

import functools

def takes_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        def true_args():
            for arg in args:
                if not isinstance(arg, (int, float)):
                    return False
            for key in kwargs:
                if not isinstance(kwargs[key], (int, float)):
                    return False    
            return True    
        # Здесь поочередно при каждом вызове add() - возвращается value
        if true_args() == True:
            value = func(*args, **kwargs)
            return value
        else: raise TypeError("Аргументы должны принадлежать типам int или float")
    return wrapper  # wrapper имеет ссылку на функцию add(), оборачивает ее, меняет ее поведение и возвращает эту обертку 



# INPUT DATA:

# TEST_1:
@takes_numbers
def mul(a, b):
    return a * b
    
print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))
print()
# TEST_2:
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
print()
# TEST_3:
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul('1', 2))
except TypeError as error:
    print(error)
print()
# TEST_4:
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul('1', '2'))
except TypeError as error:
    print(error)
print()
# TEST_5:
@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b='2'))
except TypeError as error:
    print(error)
print()
# TEST_6:
@takes_numbers
def mul(a, b=2):
    """multiplication"""
    return a * b


print(mul.__name__)
print(mul.__doc__)
print(mul(3, 4))
print()
# TEST_7:
print(takes_numbers)
print()
# TEST_8:
@takes_numbers
def mul(a, b=2):
    return a * b

print(mul(1, b=2))
    