

class User:
    
    def __init__(self, name, age):
        
        if isinstance(name, str) and name != '' and name.isalpha() : self._name = name
        else: raise ValueError("Некорректное имя")
        
        if isinstance(age, int) and age in range(0, 111): self._age = age
        else: raise ValueError('Некорректный возраст') 
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name != '' and new_name.isalpha(): self._name = new_name
        else: raise ValueError("Некорректное имя")
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age in range(0, 111): self._age = new_age
        else: raise ValueError('Некорректный возраст')    
        return self._age
    
# INPUT DATA:

# TEST_1:
user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())
print()
# TEST_2:
user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())
print()
# TEST_3:
user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
print()
# TEST_4:
user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)
print()
# TEST_5:
invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user = User(name, 37)
    except ValueError as e:
        print(e)
print()
# TEST_6:
invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50)
for age in invalid_ages:
    try:
        user = User('Меган', age)
    except ValueError as e:
        print(e)
print()
# TEST_7:
try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)    