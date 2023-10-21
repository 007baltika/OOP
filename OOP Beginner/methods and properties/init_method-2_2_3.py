#Поочередно печатаем фразы полоскабелая, полоска черная, начиная с белой (Разные зебры)

class Zebra():
    
    def __init__(self):
        self.a = 1
    
    def which_stripe(self):
        
        if self.a % 2 == 1:
            print("Полоска белая")
            self.a = self.a + 1
        else: 
            print("Полочка черная")
            self.a = self.a + 1
        
        
Console.ReadLine()           