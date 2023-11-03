# Реализуйте класс CyclicList , описывающий циклический список. При создании
# экземпляра класс должен принимать один аргумент:
# • iterable — итерируемый объект, определяющий начальный набор
# элементов циклического списка. Если не передан, начальный набор
# элементов считается пустым
# Класс CyclicList должен иметь два метода экземпляра:
# • append() — метод, принимающий в качестве аргумента произвольный
# объект и добавляющий его в конец циклического списка
# • pop() — метод, который принимает в качестве аргумента индекс
# элемента циклического списка, возвращает его значение и удаляет из
# циклического списка элемент с данным индексом. Если аргумент
# не передан, возвращаемым и удаляемым элементом считается последний
# элемент циклического списка

# При передаче экземпляра класса CyclicList в функцию len() должно
# возвращаться количество элементов в нем.
# Также экземпляр класса CyclicList должен быть зацикленным итерируемым
# объектом. Другими словами, итерация по нему должна происходить бесконечно,
# и при каждом достижении его последнего элемента она должна начинаться
# сначала.

# Наконец, экземпляр класса CyclicList должен позволять получать значения
# своих элементов с помощью индексов, при этом индексы должны работать
# циклически. Например, в циклическом списке [1, 2, 3] элементом с
# индексом 4 должно являться число 2 .

import itertools as it

class CyclicList:
    
   
    def __init__(self, iterable = []):
        self.iterable = list(iterable)
        
    def append(self, obj):
        self.iterable.append(obj)
        
    def pop(self, index = None):
        if index == None: 
            return self.iterable.pop(self.__len__() - 1)
        else: return self.iterable.pop(index)  
        
    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from it.cycle(self.iterable)
        
    def __getitem__(self, id):
        a = self.__iter__()   
        for _ in range(0, id):
            next(a)
        return next(a)    
    
    
# TEST_1:
cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')
    
print()
print()
# TEST_2:
cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))

print()
# TEST_3:
cyclic_list = CyclicList([1, 2, 3])

print(cyclic_list[1])
print(cyclic_list[2])
print(cyclic_list[5])
print(cyclic_list[12])
print()
# TEST_4:
indexes = [553, 555, 561, 606, 610, 744, 748, 766, 930, 1015, 1049, 1074, 1093, 1107, 1275, 1290, 1309, 1315, 1366,
           1398, 1552, 1573, 1629, 1639, 1651, 1656, 1755, 1792, 1857, 1909, 1918, 1919, 1937, 1949, 1997, 2002, 2085,
           2144, 2156, 2181, 2219, 2233, 2256, 2290, 2299, 2308, 2310, 2327, 2366, 2393, 2615, 2653, 2665, 2788, 2812,
           2902, 2914, 3035, 3094, 3219, 3221, 3254, 3315, 3412, 3502, 3532, 3567, 3572, 3614, 3694, 3740, 3753, 3760,
           3794, 3826, 3838, 3855, 3906, 3951, 4016, 4019, 4139, 4203, 4219, 4285, 4300, 4397, 4398, 4503, 4529, 4559,
           4587, 4589, 4710, 4747, 4783, 4785, 4790, 4890, 4995]

numbers = CyclicList([1, 2, 3, 4, 5])

numbers_list = [numbers[i] for i in indexes]
print(numbers_list)
print()
# TEST_5:
data = [537, 555, 660, 662, 764, 770, 847, 874, 895, 938, 957, 996, 1034, 1040, 1104, 1193, 1205, 1295, 1301, 1487,
        1561, 1584, 1687, 1717, 1727, 1745, 1883, 1892, 1894, 1908, 1926, 1927, 1944, 2064, 2086, 2087, 2126, 2287,
        2310, 2393, 2414, 2431, 2472, 2509, 2576, 2602, 2603, 2651, 2744, 2756, 2806, 2816, 2871, 2903, 2996, 3004,
        3005, 3036, 3086, 3142, 3213, 3279, 3490, 3530, 3534, 3554, 3619, 3664, 3718, 3772, 3816, 3836, 3953, 3966,
        4012, 4017, 4102, 4130, 4193, 4215, 4228, 4304, 4306, 4385, 4441, 4592, 4596, 4642, 4692, 4695, 4728, 4740,
        4799, 4865, 4933, 4960, 4977]

numbers = CyclicList([1, 2, 3, 4, 5])
print(len(numbers))

for item in data:
    numbers.append(item)

print(len(numbers))
print(numbers[1000], numbers[2000], numbers[3000])
print()
# TEST_6:
data = [1, 2, 3, 4, 5]
cycliclist = CyclicList(data)
data.extend([6, 7, 8, 9, 10])

count = 0
for item in cycliclist:
    if count == 10:
        break
    print(item, end=' ')
    count += 1
print()    
print()
# TEST_7:
cyclic_list = CyclicList()
cyclic_list.append(1)

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')             