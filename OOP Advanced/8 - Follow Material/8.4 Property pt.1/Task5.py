

# Реализуйте класс декоратор @exception_decorator , который возвращает

# • кортеж (value, None) , если декорируемая функция завершила свою работу без возбуждения исключения, где value — возвращаемое значение декорируемой функции
# • кортеж (None, errortype) , если во время выполнения декорируемой функции было возбуждено исключение, где errortype — тип возбужденного исключения


import functools


#КОНСТРУКЦИЯ, КОГДА КЛАСС НЕ ПОЛУЧАЕТ АРГУМЕНТ

class exception_decorator:
    
    def __init__(self, func):
        functools.update_wrapper(self, func)  # СОХРАНЕНИЕ ИНФОРМАЦИИ О ДЕКОРИРУЕМОЙ ФУНКЦИИ
        self.func = func                      # ДЕКОРИРУЕМАЯ ФУНКЦИЯ
    
    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return (value, None)
        except Exception as e:
            return (None, type(e))
    


# INPUT DATA:

# TEST_1:
@exception_decorator
def func(x):
    return 2*x + 1
    
print(func(1))
print(func('bee'))
print()
# TEST_2:
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 10))
print()
# TEST_3:
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 'stepik'))
print()
# TEST_4:
@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(f(1, 2, 3, param1=4, param2=10))
print()
# TEST_5:
@exception_decorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2='10'))
print()
# TEST_6:
sum = exception_decorator(sum)

print(sum(['199', '1', 187]))  