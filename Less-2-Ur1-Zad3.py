#Программа рассчитывает расстояние между двумя точками по теореме Пифагора
from math import *

class Point():

    def set_coordinates(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def get_distance(self, arg):
        if hasattr(arg, 'x'):
            if hasattr(arg, 'y'):
                return sqrt(pow((self.x - arg.x), 2) + pow((self.y - arg.y), 2))
            else: print("Передана не точка") 
        else: print("Передана не точка")    



Console.ReadLine() 
