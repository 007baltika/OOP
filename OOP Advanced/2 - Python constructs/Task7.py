# Функция quantify() должна считать, для скольких элементов итерируемого
# объекта iterable функция-предикат predicate вернула значение true , и
# возвращать полученный результат.

count = 0
def quantify(iterable, predicate):
    a = filter(predicate, iterable)
    return len(list(a))

# TEST_1:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(quantify(numbers, lambda x: x > 1))

# TEST_2:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(quantify(numbers, lambda x: x % 2 == 0))

# TEST_3:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(quantify(numbers, lambda x: x < 0))

# TEST_4:
# iterable = ['dddddd', 'a', 'aa', 'aaa', 'bbbb', 'ccccc']
# print(quantify(iterable, lambda elem: len(elem) > 3))

# TEST_5:
# iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])
# print(quantify(iterable, lambda elem: elem.startswith('c')))

# TEST_6:
# iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])
# print(quantify(iterable, lambda elem: elem.endswith('A')))

# TEST_7:
# iterable = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(quantify(iterable, lambda elem: elem == 1))

# TEST_8:
# iterable = iter([2, 3, 4, 5, 6, 7, 8, 9, 1])
# print(quantify(iterable, lambda elem: elem == 1))

# TEST_9:
# iterable = iter([2, 3, 4, 1, 5, 6, 7, 8, 9, 10])
# print(quantify(iterable, lambda elem: elem == 1))

# TEST_10:
# iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])
# print(quantify(iterable, None))