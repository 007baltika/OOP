
class Student():
    
    def __init__(self, name, age, branch):
            self.__name = name
            self.__age = age
            self.__branch = branch
            
    def __display_details(self):
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Профессия: {self.__branch}")  
        
    def acess_private_method(self):
        self.__display_details()
     
Console.ReadLine()           