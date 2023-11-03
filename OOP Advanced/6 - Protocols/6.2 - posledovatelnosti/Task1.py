# Реализуйте класс ReversedSequence , описывающий объект, который реализует
# доступ к элементам некоторой последовательности в обратном порядке. При
# создании экземпляра класс должен принимать один аргумент:
# • sequence — последовательность
# При передаче экземпляра класса ReversedSequence в функцию len() должна
# возвращаться его длина, представленная количеством элементов в исходной
# последовательности.

# Также экземпляр класса ReversedSequence должен быть итерируемым
# объектом, элементами которого являются элементы исходной
# последовательности в обратном порядке.

# Наконец, экземпляр класса ReversedSequence должен позволять получать
# значения элементов исходной последовательности с помощью индексов, при
# этом индексация должна производиться в обратном порядке, то есть по
# индексу 0 должен быть доступен последний элемент исходной
# последовательности, по индексу 
# 1 — предпоследний элемент, по индексу 2 — предпредпоследний элемент, и так далее.

class ReversedSequence:

    def __init__(self, sequence):
        self.sequence = sequence

        
    def __getitem__(self, id):

        if isinstance(id, int):
            return self.sequence[self.__len__() - id - 1]   
        else: raise ValueError
        
    def __len__(self):
        return len(self.sequence)
    
    def __iter__(self):
        yield from self.sequence
        
        

# TEST_1:
reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])
print()
# TEST_2:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])
print()
# TEST_3:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
print()
# TEST_4:
reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)
print()
# TEST_5:
reversed_chars = ReversedSequence('abcde')

for char in reversed_chars:
    print(char)
print()
# TEST_6:
reversed_chars = ReversedSequence('abcdefghijklmnopqrstuvwxyz')

print(reversed_chars[0], reversed_chars[7], reversed_chars[11], reversed_chars[25])
print()
# TEST_7:
reversed_list = ReversedSequence(['Gvido', 'Elon', 'Gates', 'Jobs', 'Zuckerberg'])

print(*reversed(reversed_list))