#Бесконечный итератор, начиная с 0...10...20...

class InfinityIterator():
    
    def __iter__(self):
        self.current_num = 0
        return self
    
    def __next__(self):
        num = self.current_num
        self.current_num += 10
        return num    




Console.ReadLine()  
