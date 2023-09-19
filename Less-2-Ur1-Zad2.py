#Программа - счетчик, который увеличивает числа

class Counter():
    
    def start_from(self, num = 0): 
        self.value = num
    
    def increment(self):
        self.value = self.value + 1
     
    def dislpay(self):
        print("Текущее значение счетчика = ", self.value)
        
    def reset(self):
        self.value = 0
        
Console.ReadLine()             
         