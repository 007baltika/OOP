

class AttrsIterator:
    
    def __init__(self, obj):
        
        self.obj = obj
        # print(obj.__dict__)
        self.attributs = [(attribute, obj.__dict__.get(attribute)) for attribute in obj.__dict__.keys()]
        # print(self.attributs)
        self.dict = list(self.attributs)
        self.start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < len(self.dict):
            value = self.dict[self.start]
            self.start += 1
            return value
        else: raise StopIteration
    
    
    
# TEST_1:
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)
print()
# TEST_2:
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
user = User('Debbie', 'Harry', 77)
user.profession = 'singer'
user.height = 160

attrsiterator = AttrsIterator(user)

print(*attrsiterator, sep='\n')
print()
# TEST_3:
class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))
print()
# TEST_4:
class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')   