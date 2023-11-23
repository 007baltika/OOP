


import functools

class ignore_exception:
    
    def __init__(self, *args):
        self.datatype = args
        
    def __call__(self, func):   #ПЕРЕДАЧА ДЕКОРИРУЕМОЙ ФУНКЦИИ
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)  # ВЫЗОВ ДЕКОРИРУЕМОЙ ФУНКЦИИ
                return value
            except Exception as err:
                if type(err) in self.datatype:
                    print(f'Исключение {err} обработано')
                else: raise err
        return wrapper
    
    
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x
func(0)    