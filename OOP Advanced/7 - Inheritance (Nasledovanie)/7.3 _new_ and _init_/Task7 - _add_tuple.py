

class AdvancedTuple(tuple):
    
    
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            a =  tuple(other)
            return super().__new__(AdvancedTuple, tuple(self)+a)    
    
    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            a =  tuple(other)
            return super().__new__(AdvancedTuple, a+tuple(self))
        
        
    def __iadd__(self, other):
        if hasattr(other, '__iter__'):
            a = tuple(other)
            return super().__new__(AdvancedTuple, tuple(self)+a)   
        
    def __riadd__(self, other):
        if hasattr(other, '__iter__'):
            a =  tuple(other)
            return super().__new__(AdvancedTuple, a+tuple(self))         
     
     
        
# TEST_1:
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)
print()
# TEST_2:
advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))
print()
# TEST_3:
data = [[4, 5, 6], {4: None, 5: None, 6: None}, (4, 5, 6), '456', iter([4, 5, 6]), AdvancedTuple([4, 5, 6])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    print(advancedtuple + item, end=' ')
    print(item + advancedtuple)
print()
# TEST_4:
data = ['456', [7, 8, 9], {10: None, 11: None, 12: None}, (13, 14, 15), iter([16, 17, 18]), AdvancedTuple([20, 21, 22])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    advancedtuple += item

print(advancedtuple)
print()
# TEST_5:
advancedtuple = AdvancedTuple([1, 2, 3])
advancedtuple += []
print(advancedtuple)    