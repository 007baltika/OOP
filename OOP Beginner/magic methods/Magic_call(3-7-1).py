#Сумма только float/int путем вызова экземпляра класса
class Addition():
    
    def __call__(self, *args):
        mass_nums = args
        summ = 0
        for num in mass_nums:
            if isinstance(num, (int, float)): 
                summ += num
        
        return f'Сумма переданных значений = {summ}'
        
Console.ReadLine()             
        