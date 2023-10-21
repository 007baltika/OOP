#Реализация стека - упорядоченной коллекции элементов, огранизованной по принципу последним пришел - первым вышел

class Stack():
    
    def __init__(self):
        self.values = []
    
    def push(self, item):
        self.values.append(item)
        
    def pop(self):
        if len(self.values) > 1:
            self.posl = self.values[-1] 
            self.values.pop()
            return self.posl
                
        else: print('Empty Stack')
    
    def peek(self):
        if len(self.values) > 1:
            return self.values[-1]    
        else: 
            return print('Empty Stack')         
        
    def is_empty(self):
        
        if len(self.values) > 1:
            return False   
        else: 
            return True
        
    def size(self):
        return len(self.values)   
    
    
Console.ReadLine()       