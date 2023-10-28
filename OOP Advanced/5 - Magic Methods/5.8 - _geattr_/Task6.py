# Реализуйте класс AttrsNumberObject . При создании экземпляра класс должен
# принимать произвольное количество именованных аргументов. 

# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру вкачестве атрибутов.

# Экземпляр класса AttrsNumberObject должен иметь один атрибут:
# • attrs_num — количество атрибутов, которыми обладает
# экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num

from typing import Any


class AttrsNumberObject:
    
    def __init__(self, **kwargs):
    
        for key, value in kwargs.items():
            setattr(self, key, value) 
           
    def __getattrs__(self, attr):
        if attr == 'attrs_num': return len(self.__dict__) + 1 
 
        
# TEST_1:
music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
print()
# TEST_2:
music_group = AttrsNumberObject()

print(music_group.attrs_num)
print()
# TEST_3:
music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)
print()
# TEST_4:
music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)
print()
# TEST_5:
person = AttrsNumberObject(name='Mark')
print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)       