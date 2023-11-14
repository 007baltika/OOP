# Реализуйте класс NumberList , наследника класса UserList , описывающий
# список, элементами которого могут быть лишь числа. При создании экземпляра
# класс должен принимать один аргумент:
    
# • iterable — итерируемый объект, определяющий начальный набор
# элементов экземпляра класса NumberList . Если хотя бы один элемент
# переданного итерируемого объекта не является числом, должно быть
# возбуждено исключение TypeError с текстом:
    
#     Элементами экземпляра класса NumberList должны быть числа

# Итерируемый объект может быть не передан, в таком случае начальный
# набор элементов считается пустым

# При изменении экземпляра класса NumberList с помощью индексов, операций
# сложения ( +, += ) и методов append(), extend() и insert() должна
# производиться проверка на то, что добавляемые элементы являются числами, в
# противном случае должно возбуждаться исключение TypeError с текстом:
#     Элементами экземпляра класса NumberList должны быть числа

from collections import UserList

class NumberList(UserList):
    
    def __init__(self, iterable = []):
        check = iterable.copy()
        c = 0
        for num in check:
            if isinstance(num, (int, float)):
                c+=1
        if c == len(iterable):         
            super().__init__(iterable)
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")    
        
    def __setitem__(self, id, value):
        if isinstance(value, (int, float)):
            self.data[id] = value
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")      
        
    def __add__(self, other):
        if isinstance(other, (int, float)) or other == [num for num in other if isinstance(num, (int, float))]:
            return self.data+other
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа") 
        
    def __iadd__(self, other):
        if isinstance(other, (int, float)) or other == [num for num in other if isinstance(num, (int, float))]:
            self.data += other
            return self.data
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")       
        
    def append(self, other):
        if isinstance(other, (int, float)) or other == [num for num in other if isinstance(num, (int, float))]:
            return self.data.append(other)
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа") 
        
    def extend(self, other):
        if isinstance(other, (int, float)) or other == [num for num in other if isinstance(num, (int, float))]:
            return self.data.extend(other)
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа") 
        
    def insert(self, id, value):
        if isinstance(value, (int, float)):
            return self.data.insert(id, value)
        else: 
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")  
        


# INPUT DATA:

# TEST_1:
numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)
print()
# TEST_2:
numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)
print()
# TEST_3:
try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)
print()
# TEST_4:
numberlist = NumberList([1, 2, 3])

try:
    numberlist.append('4')
except TypeError as error:
    print(error)
print()
# TEST_5:
numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)
print()
# TEST_6:
numberlist1 = NumberList([1, 2])

try:
    numberlist2 = numberlist1 + [3, '4']
except TypeError as e:
    print(e)
print()
# TEST_7:
data = [1, 2, 3]
numberlist = NumberList(data)

print(numberlist)

data.extend([4, 5, 6])
print(data)
print(numberlist)
print()
# TEST_8:
numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)
print()
# TEST_9:
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, '4', 3])
except TypeError as e:
    print(e)
print()
# TEST_10:
n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)          
        
        