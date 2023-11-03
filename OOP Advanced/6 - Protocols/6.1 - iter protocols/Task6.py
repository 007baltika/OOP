
import itertools as it
import copy

class Peekable:
    
    def __init__(self, iterable):
        # self.iterable = iterable
        self.perem_for_len = len(copy.deepcopy(list(iterable)))
        self.iterable = iter(iterable)
        self.start = 0
        
    def peek(self, default = None):
        a = list(copy.deepcopy(self.iterable))
        if a != []:
            return a[0]
        elif default != None: return default

        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.perem_for_len:
            self.start += 1
            return next(self.iterable)
        else: raise StopIteration
    

# TEST_1:
iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)
print()
# TEST_2:
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print()
# TEST_3:
iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))
print()
# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')
print()
# TEST_5:
from itertools import islice

iterator = Peekable([n ** 2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))
print()
# TEST_6:
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))
print()
# TEST_7:
from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')