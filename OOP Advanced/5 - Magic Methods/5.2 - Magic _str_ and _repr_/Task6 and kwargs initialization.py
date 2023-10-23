# Реализуйте класс AnyClass . При создании экземпляра класс должен принимать
# произвольное количество именованных аргументов и устанавливать их в
# качестве атрибутов создаваемому экземпляру.

class AnyClass:
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  
            
    def __str__(self):
        a = 'Anyclass: '
        b = []
        for key, value in self.__dict__.items():
            if type(value) != str:
                b.append(f'{key}={value}')
            else: b.append(f"{key}='{value}'")    
        return a + ', '.join(b)
        
    def __repr__(self):
        a = 'Anyclass('
        b = []
        for key, value in self.__dict__.items():
            if type(value) != str:
                b.append(f'{key}={value}')
            else: b.append(f"{key}='{value}'")    
        return a + ', '.join(b) + ')'
        
    
# TEST_1:
any = AnyClass()

print(str(any))
print(repr(any))
print()
# TEST_2:
cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))
print()
# TEST_3:
obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))
print()
# TEST_4:
obj1 = AnyClass(name='Gvido', language='Python', age=67)
obj2 = AnyClass(name='Поколение Python', language='Python', age=4, best=True)

print(obj1, obj2, sep=', ')
print([obj1, obj2])
print((obj1))
print((obj2,))
print()
# TEST_5:
attrs = {
    'name': 'Margaret Heafield Hamilton',
    'birth_date': '17.09.1936',
    'age': 86,
    'career': 'computer scientist'
}
obj = AnyClass(**attrs)
print(obj)
print()
# TEST_6:
attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)       