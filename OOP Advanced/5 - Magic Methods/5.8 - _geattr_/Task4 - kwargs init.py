# Реализуйте класс DefaultObject . При создании экземпляра класс должен
# принимать один именованный аргумент default , имеющий значение по
# умолчанию None , а после произвольное количество именованных аргументов.
# Аргументы, передаваемые после default , должны устанавливаться
# создаваемому экземпляру в качестве атрибутов.
# При обращении к несуществующему атрибуту экземпляра
# класса DefaultObject должно возвращаться значение default .

from typing import Any


class DefaultObject:
    
    def __init__(self, default = None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)        
        
    def __getattr__(self, attr):
        return self.default    
        
        
# TEST_1:
god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)
print()
# TEST_2:
god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)
print()
# TEST_3:
names = ['Martin', 'Dustin', 'John', 'John Wong', 'John Hanna', 'Theresa', 'Brittany Wheeler', 'David', 'Nancy',
         'Brian Mendez', 'Jennifer Potts', 'Kimberly Walton', 'Debbie Dominguez', 'Marissa Perez', 'Alexander',
         'Shelly', 'Michael', 'Tara', 'Cynthia', 'Jennifer', 'Jesse', 'Douglas', 'Jennifer Patel', 'James', 'Latoya',
         'Kirsten Fisher', 'Brianna', 'Sean', 'Laura', 'Brandi', 'Randall Christian', 'Teresa', 'Keith',
         'Diamond Watson', 'Anne', 'Sarah', 'Earl', 'Kerry Lane', 'Bonnie', 'Dwayne', 'Sonia', 'Mark Miller',
         'Randall Galvan', 'Mark', 'Shannon Stephenson', 'Anthony', 'Steven', 'Samantha Miller', 'Paul Wright',
         'Dennis Lewis', 'Jessica', 'Cody Perry', 'Edward', 'Robert', 'Jacob', 'Adam', 'Tamara', 'Denise Tyler DDS',
         'Angela Jones MD', 'Alexandra', 'Dennis', 'Dawn Clark', 'Kara Mcdonald', 'Anthony Perry', 'Stephanie',
         'Jonathan', 'Amy', 'Martin Collins', 'Joseph', 'Charles Sheppard', 'Shelly Mills', 'Phillip Marshall',
         'Steven Wilson', 'Kimberly Brown', 'Terry Day', 'Mrs. Victoria Dudley', 'Sara', 'Lucas Cooper', 'Brooke',
         'Raymond Gonzalez', 'Randy Moss', 'Lisa', 'Cody Smith', 'Rebecca', 'Nicole Aguilar', 'Jessica Roman',
         'Anna Mcclure MD', 'John Watts', 'Michaela Cochran', 'Penny', 'Randy Keith', 'Alexis Quinn', 'William',
         'Christopher Young', 'Emily Johnson', 'James King', 'Haley', 'Kelly Miller', 'Manuel Lopez', 'Kathleen']

unknown = 'Doe'
for name in names:
    person = name.split()
    if len(person) == 2:
        name, surname = person
        person = DefaultObject(default=unknown, name=name, surname=surname)
    else:
        person = DefaultObject(default=unknown, name=name)
    print(person.name, person.surname)
print()
# TEST_4:
god = DefaultObject(name='Kratos', mythology='greek')
print('name' in god.__dict__)
print('mythology' in god.__dict__)       