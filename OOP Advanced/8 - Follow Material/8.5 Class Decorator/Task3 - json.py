# Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен
# принимать один аргумент:

# • filename — имя json файла, содержимым которого является JSON объект

# Декоратор должен открывать файл filename и добавлять в качестве атрибута
# декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося
# в этом файле.

import json

def jsonattr(filename):
    
    def add_attr(cls):
        with open(filename, 'r') as file:
            for line in file:
                to_python = json.loads(line)
                for key, value in to_python.items():
                    setattr(cls, key, value)
        return cls 

    return add_attr



# INPUT DATA:

# TEST_1:
with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)
print()
# TEST_2:
with open('test.json', 'w') as file:
    file.write('{"name": "John", "surname": "Doe"}')


@jsonattr('test.json')
class Person:
    pass


print(Person.name)
print(Person.surname)
print()
# TEST_3:
with open('test.json', 'w') as file:
    file.write('{"name": "Кемаль", "breed": "Британский"}')


@jsonattr('test.json')
class Cat:
    def __init__(self, name=None, breed=None):
        self.name = name or self.name
        self.surname = breed or self.breed


cat = Cat()
print(cat.name)
print(cat.breed)
print()
# TEST_4:
with open('test.json', 'w') as file:
    file.write('{"shoot1": "pif", "shoot2": "paf"}')


@jsonattr('test.json')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()