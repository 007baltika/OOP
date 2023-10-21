#Программа, которая использует декоратор для функции и возвращает время, за которое програма проработала

import time

class Timer:
    
    def __init__(self, calculate_func):
        self.calculate_func = calculate_func
    
    def __call__(self):
        self.calculate_func()
        
@Timer
def calculate():
    for i in range(10000000):
        2**100
        if i == 999999: print('999999 passed')
            
calculate()
print(time.time())            