

class Person:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
    @fullname.setter
    def fullname(self, new_family):
        self.name, self.surname = new_family.split()
    
# TEST_1:
person = Person('Mike', 'Pondsmith')

print(person.name)
print(person.surname)
print(person.fullname)
print()
# TEST_2:
person = Person('Mike', 'Pondsmith')

person.name = 'Troy'
print(person.fullname)
print()
# TEST_3:
person = Person('Mike', 'Pondsmith')

person.surname = 'Baker'
print(person.fullname)
print()
# TEST_4:
person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)
print()
# TEST_5:
person = Person('Margaret', 'Hamilton')

print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))    