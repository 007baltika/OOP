#Получаем на вход доллары и центы, впоследствии программа должна получать новые доллары и центы и перезаписывать их

class Money():
    
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents
        self._total_cents = (self._dollars * 100) + self._cents
    
    @property    
    def total_cents(self):
        return (self._dollars * 100) + self._cents   
        
    @property
    def dollars(self):
        return self._dollars
    
    @dollars.setter
    def dollars(self, new_dollars):
        if not isinstance(new_dollars, int) and new_dollars < 0:
            raise ValueError("Error dollars")
        else: 
            self._dollars = new_dollars
            self._total_cents = (self._dollars * 100) + self._cents
        
    @property 
    def cents(self):
        return self._cents
    
    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 <= new_cents < 100:
            self._cents = new_cents
            self._total_cents = (self._dollars * 100) + self._cents
            
        else: 
            raise ValueError("Error cents")
        
    def __str__(self):
        return f'Ваше состояние составляет {self._dollars} долларов {self._cents} центов'    
    
#Console.ReadLine()    
            