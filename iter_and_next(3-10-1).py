#Степень двойки по указанной степени

class PowerTwo():
    
    def __init__(self, power):
        self.power = power
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index > self.power:
            return ValueError
        else: 
            curren_num = 2 ** self.index
            self.index += 1
        return curren_num
    
Console.ReadLine()          