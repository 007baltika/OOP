#Практика по геттерам и сеттерам, проверка на валидный email

class UserMail():
    
    def __init__(self, login, email):
        self.login = login
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        
        ind_a = email.index("@")
        ind_point = email.index(".")
        
        count_a = email.count('@')
        count_point = email.count('.')
        
        if not isinstance(email, str) or ((ind_a > ind_point) or count_a != 1 or count_point != 1):
            raise ValueError("Вы должны ввести строку, включающую символы @ и . последовательно")
        else:
            self.__email = email
            
    email = property(fget = get_email, fset = set_email)    
    
    
Console.ReadLine()          