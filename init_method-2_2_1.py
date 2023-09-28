#Непонятно зачем

class Laptop():
    def __init__(self, brand = 'a', model = 'b', price = 'c'):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + self.model
        
laptop1 = Laptop()
laptop2 = Laptop()

Console.ReadLine()           