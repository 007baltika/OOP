# Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-
# b , где a — левая граница диапазона, b — правая граница диапазона, причем a
# <= b . Диапазон содержит в себе все числа от a до b включительно. 

# Например, диапазон 1-4 содержит числа 1, 2, 3 и 4 .

# Реализуйте класс CustomRange , описывающий последовательность, элементами
# которой являются одиночные целые числа и числа из определенных
# диапазонов. При создании экземпляра класс должен принимать произвольное
# количество позиционных аргументов, каждый из которых является одиночным
# целым числом либо диапазоном.

# При передаче экземпляра класса CustomRange в функцию len() должно
# возвращаться количество элементов в нем. При передаче экземпляра
# класса CustomRange в функцию reversed() должен возвращаться итератор,
# элементами которого являются элементы переданного экземпляра
# класса CustomRange , расположенные в обратном порядке.

# Экземпляр класса CustomRange должен быть итерируемым объектом, то есть
# позволять перебирать свои элементы, например, с помощью цикла for .

# Помимо этого, экземпляр класса CustomRange должен поддерживать операцию
# проверки на принадлежность с помощью оператора in .

# Наконец, экземпляр класса CustomRange должен позволять получать значения
# своих элементов с помощью индексов, причем как как положительных, так и
# отрицательных



from collections import UserList

class CustomRange(UserList):
    
    def __init__(self, *args):
        # '1-5' -> превращается в range(1, 6) -> превращается в список [1, 2, 3, 4, 5]
        a = list(map(lambda x: list( range( [int(num) for num in x.split('-')][0], [int(num) for num in x.split('-')][1]+1)) if isinstance(x, str) else int(x) , args))
        iterable = []
        #обьединяем список и int в один список iterable
        for num in a:
            if isinstance(num, list):
                for n in num:
                    iterable.append(n)
            else: iterable.append(num)
        super().__init__(iterable)        
    
    def __len__(self):
        return len(self.data)
    
    def __reversed__(self):
        return iter(self.data[::-1])
    
    def __iter__(self):
        yield from self.data
        
    def __contains__(self, obj):
        return obj in self.data
    
    def __getitem__(self, index):
        return self.data[index]    
    


# INPUT DATA:

# TEST_1:
customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])
print()
# TEST_2:
customrange = CustomRange(1, '2-5', 3, '1-4')

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)
print()
# TEST_3:
customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))
print()
# TEST_4:
customrange = CustomRange('0-1000')

print(len(customrange))
print(*customrange)
print()
# TEST_5:
customrange = CustomRange('0-50', '25-75', '50-100')

for digit in customrange:
    print(digit, end=' ')
print()
# TEST_6:
customrange = CustomRange(1, 212, '89-323', 87, '17-82', 124, '300-312', 832, 1234)

print(*customrange)
print(customrange[11])
print(customrange[44])
print(customrange[-12])
print(customrange[-38])
print(82 in customrange)
print(17 in customrange)