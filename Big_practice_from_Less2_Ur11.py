#Программа которая регистрирует пользователя с безопасным паролем
#Программа включает в себя исключения, исходя из которых пользователь должен подобрать пароль
#Программа включает в себя файл с небезопасными паролями easy_passwords.txt и сравнивает полученный пароль на нахождение в этом файле
#Логин не проходит проверку на позицию @ и . но эта реализация была проделана мною в предыдущих дз

class Registration():

    #Чтобы не было проблем с рекурсией, делаю переменные приватными
    #А для того чтобы программа шла сразу в сеттер, делаю из переменной свойство 
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    @property
    def login(self):
        return self.__login   
    
    @login.setter
    def login(self, new_login):
        if '@' not in new_login: raise ValueError("Login must include at least one '@'")
        elif '.' not in new_login: raise ValueError("Login must include at least one '.'")
        else: self.__login = new_login
    
    @property
    def password(self):
        return self.__password
    
    @staticmethod
    def is_include_digit(new_password):
        count_nums = 0
        for i in range(0, len(new_password)):
            if new_password[i] in '0123456789':
                count_nums += 1
        if count_nums > 0: 
            return True
        else: return False
    
    #Проблема с рекурсией не здесь 
    @staticmethod
    def is_include_all_register(new_password):
        count_register_A = 0
        count_register_a = 0
        for j in range(0, len(new_password)):
            if new_password[j] in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
                count_register_A += 1
            if new_password[j] in 'qwertyuioplkjhgfdsazxcvbnm':
                count_register_a += 1
                    
        if count_register_A > 1 and count_register_a > 0:
            return True
        else: return False
    
    # Проблема с рекурсией не здесь        
    @staticmethod
    def is_include_only_latin(new_password):
        count_register = 0
        for k in range(0, len(new_password)):
            if 32 < ord(new_password[k]) < 127:
                count_register += 1        
        if count_register == len(new_password):
            return True
        else: return False
        
    @staticmethod
    def check_password_dictonary(new_password):
        flag = True
        with open('easy_passwords.txt') as file:
            mass_lines = file.readlines()
            file.seek(0)
            for i in range(0, len(mass_lines)):   
                if file.readline().rstrip() not in new_password:
                    continue
                else: 
                    flag = False
        return flag
    
    
    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str): raise ValueError("Пароль должен быть строкой")
        if not (4 < len(new_password) < 12): raise ValueError("Пароль должен быть длиннее 4 и меньше 12 символов") 
        if not Registration.is_include_digit(new_password) == True: raise ValueError("Пароль должен содержать хотя бы одну цифру") 
        if not Registration.is_include_all_register(new_password) == True: raise ValueError("Пароль должен содержать хотя бы две заглавные буквы и одну строчную букву") 
        if not Registration.is_include_only_latin(new_password) == True: raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictonary(new_password) == True: raise ValueError("Ваш пароль содержиться в списке самых легких")
        self.__password = new_password
        
Console.ReadLine()         
        