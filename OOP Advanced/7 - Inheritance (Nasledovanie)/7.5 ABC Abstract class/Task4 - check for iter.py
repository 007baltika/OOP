

from collections.abc import *

# Функция должна возвращать true , если объект obj является итерируемым
# объектом, или false в противном случае.
def is_iterable(obj):
    
    # if hasattr(obj, '__iter__'):
    #     return True
    # else: return False
    
    return isinstance(obj, Iterable)


# Функция должна возвращать true , если объект obj является итератором,
# или false в противном случае.    
def is_iterator(obj):
    
    # if hasattr(obj, '__next__'):
    #     return True
    # else: return False 
    
    return isinstance(obj, Iterator)   
    
      
# INPUT DATA:

# TEST_1:
print(is_iterable(123))
print(is_iterable([1, 2, 3]))
print(is_iterable((1, 2, 3)))
print(is_iterable('123'))
print(is_iterable(iter('123')))
print(is_iterable(map(int, '123')))
print()
# TEST_2:
print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))