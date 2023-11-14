
# Класс SuperInt должен иметь четыре метода экземпляра:

# • repeat() — метод, принимающий в качестве аргумента целое число n ,
# по умолчанию равное 2 , и возвращающий экземпляр класса SuperInt ,
# продублированный n раз
# • to_bin() — метод, возвращающий двоичное представление экземпляра
# класса SuperInt . Двоичное представление может быть как в виде
# экземпляра класса str , так и int
# • next() — метод, возвращающий новый экземпляр класса SuperInt ,
# который больше текущего на единицу
# • prev() — метод, возвращающий новый экземпляр класса SuperInt ,
# который меньше текущего на единицу

# Также экземпляр класса SuperInt должен быть итерируемым объектом,
# элементами которого являются его цифры слева направо. Сами цифры так же
# должны быть представлены в виде экземпляров класса SuperInt .


class SuperInt(int):
    
    start = 0
    
    def repeat(self, n=2):
        if self < 0:
            return -SuperInt(str(abs(self)) * n)
        else: 
            return SuperInt(str(self) * n)
    
    def to_bin(self):
        if self >= 0:
            return SuperInt(bin(int(self))[2:])
        else:
            return -SuperInt(bin(int(self))[3:])
    
    def next(self):
        new_example = super().__new__(SuperInt, self+1)
        return new_example
    
    def prev(self):
        new_example = super().__new__(SuperInt, self-1)
        return new_example
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < len(str(abs(self))):
            value = str(abs(self))[self.start]
            self.start += 1
            return SuperInt(value)
        else: 
            self.start = 0
            raise StopIteration
        
# INPUT DATA:

# TEST_1:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))
print()
# TEST_2:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())
print()
# TEST_3:
superint = SuperInt(17)

print(superint.prev())
print(superint.next())
print()
# TEST_4:
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
print()
# TEST_5:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
superint = SuperInt(30)

for n in digits:
    print(superint.repeat(n))
print()
# TEST_6:
superint = SuperInt(30)

for i in range(10):
    superint = superint.next()
    print(superint)
print()
# TEST_7:
superint = SuperInt(30)

for i in range(10):
    superint = superint.prev()
    print(superint)
print()
# TEST_8:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(superint.to_bin())
print()
# TEST_9:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(superint.to_bin())
print()
# TEST_10:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(*superint)
print()
# TEST_11:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(*superint)
print()
# TEST_12:
superint = SuperInt(100)
print(type(superint))
print(type(superint.next()))
print(type(superint.prev()))
print(type(superint.repeat()))
print()
# TEST_13:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))
    
    