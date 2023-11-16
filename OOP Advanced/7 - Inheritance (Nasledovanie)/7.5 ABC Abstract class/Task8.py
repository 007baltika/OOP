
from collections import UserList

class SortedList(UserList):
    
    def __init__(self, iterable = []):
        super().__init__(sorted(iterable))
        
    def add(self, obj):
        self.data.append(obj)
        
    def discard(self, obj):
        while obj in self.data:
            self.data.remove(obj)
            
    def update(self, obj):
        self.data.extend(obj)
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data
        
    def __contains__(self, obj):
        return obj in self.data
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        raise NotImplementedError("Неподдерживаемая операция") 
    
    def __delitem__(self, index):
        del self.data[index]
        
    def __add__(self, iterable):
        if not isinstance(iterable, (list, SortedList)): return 'NotImplemented'
        return SortedList(sorted(sorted(self.data)+(sorted(iterable))))  
    
    def __iadd__(self, iterable):
        if not isinstance(iterable, (list, SortedList)): return 'NotImplemented'
        return SortedList(sorted(self.data + iterable))    
    
    def __mul__(self, n):
        if not isinstance(n, int): return 'NotImplemented'
        return SortedList(sorted(self.data * n))
    
    def __imul__(self, n):
        if not isinstance(n, int): return 'NotImplemented'
        return SortedList(sorted(self.data * n))
    
    def append(self, *args): raise NotImplementedError("Неподдерживаемая операция") 
    def insert(self, *args): raise NotImplementedError("Неподдерживаемая операция")  
    def extend(self, *args): raise NotImplementedError("Неподдерживаемая операция")  
    def reverse(self): raise NotImplementedError("Неподдерживаемая операция")  
    def __reversed__(self): raise NotImplementedError("Неподдерживаемая операция")  
    
    def __repr__(self):
        return f"SortedList({sorted(self.data)})"
    
    

    
# INPUT DATA:

# TEST_1:
numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)
print()
# TEST_2:
numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)
print()
# TEST_3:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)
print()
# TEST_4:
numbers = SortedList([5, 4, 3, 2, 1])

print(numbers)
del numbers[1]

print(numbers)
del numbers[-1]

print(numbers)

try:
    numbers[0] = 7
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_5:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.append(6)
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_6:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.insert(0, 0)
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_7:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.extend([6, 7, 8, 9, 10])
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_8:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.reverse()
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_9:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    reversed(numbers)
except NotImplementedError:
    print('Неподдерживаемая операция')
print()
# TEST_10:
numbers = SortedList([5, 4, 3, 2, 1])
numbers.update([5, 4, 3, 2, 1])
print(*numbers)
numbers *= 3
print(*numbers)
numbers.discard(4)
print(*numbers)
print()
# TEST_11:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)
print()
# TEST_12:
data = [5, 4, 3, 2, 1]
numbers = SortedList(data)

print(numbers)
data.pop()

print(data)
print(numbers)
print()
# TEST_13:
numbers = SortedList()
print(numbers)
print()
# TEST_14:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 + numbers2
print(numbers1, type(numbers1))

numbers2 = numbers2 * 2
print(numbers2, type(numbers2))
print()
# TEST_15:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 += numbers2
print(numbers1, type(numbers1))

numbers2 *= 2
print(numbers2, type(numbers2))
print()
# TEST_16:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 * -100
print(numbers1)

numbers2 *= 0
print(numbers2)
print()
# TEST_17:
numbers = SortedList([5, 3, 4, 2, 1])
print(numbers.__add__(1))
print(numbers.__iadd__(1.1))
print(numbers.__mul__([1, 2, 3]))
print(numbers.__imul__({4, 5, 6}))    
                 