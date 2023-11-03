# Реализуйте класс SkipIterator . При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:
# • iterable — итерируемый объект
# • n — целое неотрицательное число
# Экземпляр класса SkipIterator должен являться итератором, который
# генерирует элементы итерируемого объекта iterable , пропуская
# по n элементов, а затем возбуждает исключение StopIteration .

class SkipIterator:
    
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < len(self.iterable):
            self.start += self.n + 1
            if self.start - self.n - 1 < len(self.iterable):
                return self.iterable[self.start - self.n - 1]
        else: raise StopIteration
        
# TEST_1:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)
print()
# TEST_2:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)
print()
# TEST_3:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)
print()
# TEST_4:
skipiterator = SkipIterator('abcd', 0)

print(*skipiterator)
print()
# TEST_5:
skipiterator = SkipIterator(['abcd'], 1)

print(*skipiterator)
print()
# TEST_6:
skipiterator = SkipIterator('abcd', 3)

print(*skipiterator)
print()
# TEST_7:
skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)
print()
# TEST_8:
skipiterator = SkipIterator(iter(['aa', 'bb', 'cc', 'dd', 'ee', 'ff']), 2)

print(*skipiterator)
print()
# TEST_9:
data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)

print(*skipiterator)
print()
# TEST_10:
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))