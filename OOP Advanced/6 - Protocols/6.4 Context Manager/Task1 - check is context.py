
# Проверка что передаваемый объект - конекстный менеджер

def is_context_manager(obj):
    if hasattr(obj, '__enter__') and hasattr(obj, '__exit__'):
        return True
    else: return False






# INPUT DATA:

# TEST_1:
print(is_context_manager(open('output.txt', mode='w')))
print()
# TEST_2:
from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    print(is_context_manager(file))
print()
# TEST_3:
from threading import Lock

print(is_context_manager(Lock()))
print()
# TEST_4:
print(is_context_manager(1992))
print(is_context_manager('beegeek'))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({'one': 1, 'two': 2}))
print(is_context_manager(None))
print()
# TEST_5:
class ContextManager:
    def __enter__(self):
        return 'beegeek'

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True
        

print(is_context_manager(ContextManager()))
print()
# TEST_6:
class ContextManager:
    def __init__(self):
        self.inside = False
  
    def __enter__(self):
        self.inside = True
        return self
  
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True
        
        
print(is_context_manager(ContextManager()))
print()
# TEST_7:
class ContextManager:
    def __enter__(self):
        return 'beegeek'


print(is_context_manager(ContextManager()))
print()
# TEST_8:
class ContextManager:
    def __init__(self):
        self.inside = False
  
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True
        
        
print(is_context_manager(ContextManager()))