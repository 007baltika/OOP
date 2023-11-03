# Реализуйте класс AttrDict , описывающий упрощенный словарь, значения
# элементов которого можно получать как по ключам ( [key] ), так и по
# одноименным атрибутам ( .key ). При создании экземпляра класс должен
# принимать один аргумент:
# data — словарь, определяющии начальныи набор элементов
# упрощенного словаря. Если не передан, начальныи набор элементов
# считается пустым
# При передаче экземпляра класса AttrDict в функцию len() должно
# возвращаться количество элементов в нем.
# Также экземпляр класса AttrDict должен быть итерируемым объектом, то есть
# позволять перебирать свои ключи, например, с помощью цикла for .
# Наконец, экземпляр класса AttrDict должен позволять получать значения
# своих элементов как по их ключам, так и по одноименным
# атрибутам. Реализовывать добавление элементов и изменение их значений по
# одноименным атрибутам не нужно.

from typing import Any


class AttrDict:
    
    def __init__(self, data = None):
        if data != None:
            self.data = dict(data)
            for name, value in self.data.items():
                setattr(self, str(name), value)
        else: 
            self.data = dict()      
    
    def __getitem__(self, attr):
        # return self.data.get(attr, KeyError)
        return getattr(self, attr)
    
    def __setitem__(self, key, value):
        self.data[key] = value
        setattr(self, str(key), value)
        
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data    
    
    
# TEST_1:
attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))
print()
# TEST_2:
attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)
print()
# TEST_3:
attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)
print()
# TEST_4:
d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')
print()
# TEST_5:
d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)




# def __getattribute__(self, attr):
#     return object.__getattribute__(self, attr)

# def __setattr__(self, attr, value):
#     print(f'Изменение значения атрибута {attr} на {value}')
#     object.__setattr__(self, attr, value)
    

      
  


        