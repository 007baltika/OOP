# экземпляры класса Vector должны поддерживать операции сравнения с
# помощью операторов == и != . Два вектора считаются равными, если их
# координаты по обеим осям совпадают. Методы, реализующие операции
# сравнения, должны уметь сравнивать как два вектора между собой, так и вектор с
# кортежем из двух чисел, представляющих координаты x и y.

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1] and len(other) == 2
        return NotImplemented
    
# TEST_1:
a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)
print()
# TEST_2:
a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
print()
# TEST_3:
a = Vector(1, 2)
pair1 = (1, 2)
pair2 = ('1', '2')
pair3 = (5, 6)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print()
# TEST_4:
vectors = [Vector(196, 21), Vector(102, 82), Vector(91, 28), Vector(137, 128), Vector(97, 69), Vector(79, 29), Vector(93, 62), Vector(85, 58), Vector(46, 176), Vector(84, 197)]
pairs = [(26, 86), (177, 150), (144, 175), (137, 128), (110, 196), (79, 29), (93, 62), (36, 158), (180, 24), (84, 167)]

for vector, pair in zip(vectors, pairs):
    print(vector == pair, vector != pair)
print()
# TEST_5:
vectors1 = [Vector(114, 220), Vector(180, 148), Vector(85, 58), Vector(49, 246), Vector(110, 250), Vector(50, 91), Vector(60, 55), Vector(75, 238), Vector(189, 88), Vector(33, 190)]
vectors2 = [Vector(148, 144), Vector(169, 296), Vector(85, 58), Vector(172, 94), Vector(191, 55), Vector(50, 91), Vector(181, 150), Vector(43, 167), Vector(98, 238), Vector(33, 190)]

for v1, v2 in zip(vectors1, vectors2):
    print(v1 == v2, v1 != v2)
print()
# TEST_6:
a = Vector(0, 1)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]

for item in not_supported:
    print(a == item)
print()
# TEST_7:
a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)
print()
# TEST_8:
vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
print(vector.__gt__(range(5)))
print(vector.__lt__([1, 2, 3]))
print(vector.__ge__({4, 5, 6}))
print(vector.__le__({1: 'one'}))   