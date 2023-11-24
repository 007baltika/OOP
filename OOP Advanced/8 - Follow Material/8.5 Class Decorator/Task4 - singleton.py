# Реализуйте декоратор @singleton для декорирования класса. Декоратор
# должен превращать декорируемый класс в синглтон, то есть в класс, при первом
# вызове создающий единственный свой экземпляр и при последующих вызовах
# возвращающий его же.

def singleton(cls):
    
    _examples = {}
    
    def get_instance(*args, **kwargs):
        if cls not in _examples:
            _examples[cls] = cls(*args, **kwargs)
        return _examples[cls]
    return get_instance

# INPUT DATA:

# TEST_1:
@singleton
class MyClass:
    pass
    
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)
print()
# TEST_2:
@singleton
class MyClass:
    pass


instances = [MyClass() for _ in range(100)]
obj = MyClass()
print(all(instance is obj for instance in instances))
print()
# TEST_3:
@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))