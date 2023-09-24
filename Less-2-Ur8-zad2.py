
class Date():
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'
    
    @property
    def usa_date(self):
        return f"{self.month:02}-{self.day:02}-{self.year:04}"    

Console.ReadLine()  