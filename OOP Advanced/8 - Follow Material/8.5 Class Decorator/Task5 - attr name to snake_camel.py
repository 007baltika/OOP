# Snake Case — стиль написания составных слов, при котором несколько слов
# разделяются символом нижнего подчеркивания ( _ ) и не имеют пробелов в
# записи, причём каждое слово пишется с маленькой буквы.

# Например, bee_geek и hello_world .

# Upper Camel Case — стиль написания составных слов, при котором несколько слов
# пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы.

# Например, BeeGeek и HelloWorld .

# Реализуйте декоратор @snake_case для декорирования класса. 
# Декоратор должен принимать один аргумент:
# attrs — булево значение, по умолчанию равняется false

# Декоратор должен переименовать все не магические методы в декорируемом
# классе, меняя их стиль написания c Camel Case и Lower Camel Case на Snake case.

# Параметр attrs должен определять, будут ли аналогичным образом
# переименованы атрибуты класса. Если он имеет значение true , стиль написания
# имен атрибутов класса должен поменяться с Camel Case и Lower Camel Case на
# Snake case, если false — остаться прежним.



# ОТ СЕБЯ: ЕСЛИ TRUE, ТО МЕНЯЕМ ВСЕ АТРИБУТЫ И МЕТОДЫ В snake_case, ЕСЛИ FALSE, ТО МЕНЯЕМ ТОЛЬКО НАЗВАНИЯ МЕТОДОВ В snake_case

import re

def snake_case(attrs = False):
    
    def decorator(cls):
        
        for methods in dir(cls):
            
            if methods[-1] != '_':
                
                obj = getattr(cls, methods)
                
                if callable(obj):
                
                    def to_snake_case(name):
                        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
                        name = re.sub('__([A-Z])', r'_\1', name)
                        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
                        return name.lower()

                    delattr(cls, methods)
                    setattr(cls, to_snake_case(methods), obj)
                    
                if attrs == True:
                    
                    if not callable(obj):  
                        
                        def to_snake_case(name):
                            name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
                            name = re.sub('__([A-Z])', r'_\1', name)
                            name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
                            return name.lower()

                    delattr(cls, methods)
                    setattr(cls, to_snake_case(methods), obj)  
                        
                                           
        return cls
    return decorator
        


# INPUT DATA:

# TEST_1:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1
    
    def superSecondMethod(self):
        return 2

obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())
print()
# TEST_2:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)
print()
# TEST_3:
@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())
print()
# TEST_4:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = 'John Doe'


obj = MyClass()
print(obj.MyName)

myclass_attrs = ['FirstAttr', 'superSecondAttr']

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print('атрибут отсутствует')
print()
# TEST_5:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

myclass_attrs = ['FirstMethod', 'superSecondMethod']

for method in myclass_attrs:
    try:
        print(obj.__dict__[method])
    except KeyError:
        print('метод отсутствует')
print()
# TEST_6:
@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())