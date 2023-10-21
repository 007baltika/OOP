
def hash_function(password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9

class Account:
    
    def __init__(self, login, parol):
        self._login = login
        self._password = parol
        
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, new_login):
        if new_login != None: raise AttributeError("Изменение логина невозможно")
    
    @property
    def password(self):
        return hash_function(self._password)
    
    @password.setter
    def password(self, new_password):
        self._password = new_password
        return self._password   
    
# TEST_1:
account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)
print()
# TEST_2:
account = Account('timyr-guev', 'lovebeegeek')

print(account.password)
account.password = 'verylovebeegeek'
print(account.password)
print()
# TEST_3:
account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)
print()
# TEST_4:
account = Account('svvaliv', 'no_one_will_know_my_password')
try:
    account.login = 'vzohan'
except AttributeError as e:
    print(e)
print()
# TEST_5:
account = Account('gvido', 'van_rossum')

print(hasattr(account, 'login'))
print(hasattr(account, 'password'))    