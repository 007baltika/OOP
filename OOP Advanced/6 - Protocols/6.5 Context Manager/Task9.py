#Надо доделать


import copy
class Atomic:

    
    def __init__(self, data, deep = False):
        self.data = data
        self.safe = copy.deepcopy(data)
        self.deep = deep
            
    def __enter__(self):
        return self.data
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        if exc_type != None:
            self.data = self.safe
            return True
        return False    
    
    


numbers = [1, 2, 3, 4, 5]
with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]
print(numbers)        
print()
numbers = [1, 2, 3, 4, 5]
with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100] # обращение по несуществующему индексу
print(numbers)