# Реализуйте класс AdvancedList , наследника класса list , описывающий список
# с дополнительным функционалом. Процесс создания экземпляра
# класса AdvancedList должен совпадать с процессом создания экземпляра
# класса list .

# Класс AdvancedList должен иметь три метода экземпляра:
    
# • join() — метод, объединяющий все элементы экземпляра
# класса AdvancedList в строку и возвращающий полученный результат.
# Метод должен принимать один строковый аргумент, по умолчанию
# равный пробелу, который является разделителем элементов списка в
# результирующей строке
# • map() — метод, принимающий в качестве аргумента функцию func и
# применяющий ее к каждому элементу экземпляра класса AdvancedList .
# Метод должен изменять исходный экземпляр класса AdvancedList , а не
# возвращать новый
# • filter() — метод, принимающий в качестве аргумента функцию func и
# удаляющий из экземпляра класса AdvancedList те элементы, для
# которых функция func вернула значение false . Метод должен изменять
# исходный экземпляр класса AdvancedList , а не возвращать новый


from collections import UserList

class AdvancedList(UserList):
    
    def __init__(Self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def join(self, sep = ' '):
        return sep.join([str(num) for num in self])
    
    def map(self, func):
        self.data = [func(num) for num in self]
    
    def filter(self, func):
        self.data = [num for num in self if func(num)]
    
    


# INPUT DATA:

# TEST_1:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join('-'))
print()
# TEST_2:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
print()
# TEST_3:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)
print()
# TEST_4:
advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)
print()
# TEST_5:
advancedlist = AdvancedList([1, 2, 3, 4, 5])
separators = [' - ', ' + ', ' = ', ' * ', ' / ', ' ! ', ' 0 ', ' & ', ' ^ ', ' -> ']

for separator in separators:
    print(advancedlist.join(separator))
print()
# TEST_6:
advancedlist = AdvancedList(['hello', 'Gvido', 'how', 'are', 'you'])
advancedlist.map(len)
print(advancedlist)