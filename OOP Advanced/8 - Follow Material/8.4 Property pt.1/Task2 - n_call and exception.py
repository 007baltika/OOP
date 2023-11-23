# Реализуйте класс декоратор @limited_calls , который принимает один
# аргумент:
# • n — целое число

# Декоратор должен разрешать вызывать декорируемую функцию n раз. Если
# декорируемая функция вызывается более n раз, должно быть возбуждено
# исключение MaxCallsException с текстом: Превышено допустимое количество вызовов

# Примечание: Не забывайте про то, что декоратор не должен поглощать
# возвращаемое значение декорируемой функции, а также должен уметь
# декорировать функции с произвольным количеством позиционных и
# именованных аргументов.



import functools

class MaxCallsException(Exception):
    pass

count = 0
def limited_calls(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Здесь поочередно при каждом вызове add() - возвращается value
            global count
            count += 1
            if count <= n:
                value = func(*args, **kwargs)
                return value
            else: 
                raise MaxCallsException("Превышено допустимое количество вызовов") 
            
        return wrapper  # wrapper имеет ссылку на функцию add(), оборачивает ее, меняет ее поведение и возвращает эту обертку 
    global count
    count = 0
    return decorator # возвращаем обертку - декоратор   


    
# INPUT DATA:

# TEST_1:
@limited_calls(3)
def add(a, b):
    return a + b
    
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)
print()
# TEST_2:
import random


@limited_calls(5)
def positive_sum(*args):
    return sum(args)


for _ in range(4):
    positive_sum(*(random.randint(1, 100) for _ in range(10)))

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

try:
    print(positive_sum(10, 124, 124, 786, 11))
except MaxCallsException as e:
    print(e)
print()
# TEST_3:
@limited_calls(5)
def concat(a, b, c):
    return a + b + c


for _ in range(5):
    print(concat('123', '456', '789'))

try:
    print(concat('123', '456', '789'))
except MaxCallsException as e:
    print(e)
print()
# TEST_4:
@limited_calls(10)
def power(a, n):
    return a ** n


for _ in range(10):
    power(2, 3)

try:
    print(power(2, 3))
except MaxCallsException as e:
    print(e)
print()
# TEST_5:
@limited_calls(10)
def power(a, n):
    """degree"""
    return a ** n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))        