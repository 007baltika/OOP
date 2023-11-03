#Надо доделать

class OrderedSet:
    
    def __init__(self, iterable = None):
        if iterable != None: self.iterable = sorted(set(iterable))
        else: self.iterable = set()
        
    def add(self, obj):

        self.iterable.add(obj)
        
    def discard(self, obj):
        self.iterable.discard(obj)
        # self.iterable = 
        
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        yield from self.iterable
        
    def __contains__(self, obj):
        return obj in self.iterable
    
    def __eq__(self, obj):
        if isinstance(obj, OrderedSet):
            return self.iterable == obj.iterable
        elif isinstance(obj, set):
            if self.iterable == sorted(self.iterable) and obj == sorted(obj):
                return sorted(self.iterable) == sorted(obj)
            elif self.iterable == sorted(self.iterable) or obj == sorted(obj):
                return len(self.iterable) == len(obj) and self.iterable == obj
        else: return NotImplemented   
        
# INPUT DATA:

# TEST_1:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))
print()
# TEST_2:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)
print()
# TEST_3:
orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)
print()
# TEST_4:
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)
print()
# TEST_5:
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))
print()
# TEST_6:
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)
print()
# TEST_7:
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))