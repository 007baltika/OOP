

import copy

class LoopTracker:
    
    def __init__(self, iterable):
        self.count = 0
        self.errors = 0
        self.start = 0
        
        self.iterable = iterable
        print(self.iterable)
        self.current_generator = []
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if  self.start < len(self.iterable):
            self.start += 1
            self.count += 1
            
            self.current_generator.append(self.iterable[self.start-1])
            return self.iterable[self.start-1]
        
        else: 
            self.errors += 1
            raise StopIteration
    
    def is_empty(self):
        if len(list(copy.deepcopy(self.__iter__()))) == 0 :
            return True
        else: return False
    
    @property
    def accesses(self):
        return self.count
    
    @property
    def empty_accesses(self):
        return self.errors
    
    @property
    def first(self):
        if self.iterable != []:
            first_element = copy.deepcopy(iter(self.iterable))
            return next(first_element)
        else: raise AttributeError("Исходный итерируемый объект пуст")
    
    @property
    def last(self):
        if self.current_generator != []: 
            return self.current_generator[-1]
        else: 
            raise AttributeError("Последнего элемента нет")



# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())
print()        
        
# # TEST_1:
# loop_tracker = LoopTracker([1, 2, 3])

# print(next(loop_tracker))
# print(list(loop_tracker))
# print()
# # TEST_2:
# loop_tracker = LoopTracker([1, 2, 3])

# print(loop_tracker.accesses)
# next(loop_tracker)
# next(loop_tracker)
# print(loop_tracker.accesses)
# print()
# # TEST_3:
# loop_tracker = LoopTracker([1, 2, 3])
# print(loop_tracker.first)

# print(next(loop_tracker))
# print(loop_tracker.first)

# print(next(loop_tracker))
# print(loop_tracker.first)

# print(next(loop_tracker))
# print(loop_tracker.first)
# print()
# # TEST_4:
# loop_tracker = LoopTracker([1, 2, 3])

# print(next(loop_tracker))
# print(loop_tracker.last)

# print(next(loop_tracker))
# print(loop_tracker.last)

# print(next(loop_tracker))
# print(loop_tracker.last)
# print()
# # TEST_5:
# loop_tracker = LoopTracker([1, 2])

# print(loop_tracker.empty_accesses)
# next(loop_tracker)
# next(loop_tracker)

# for _ in range(5):
#     try:
#         next(loop_tracker)
#     except StopIteration:
#         pass
        
# print(loop_tracker.empty_accesses)
# print()
# # TEST_6:
# loop_tracker = LoopTracker([1, 2])

# print(loop_tracker.is_empty())
# next(loop_tracker)
# print(loop_tracker.is_empty())
# next(loop_tracker)
# print(loop_tracker.is_empty())
# print()
# # TEST_7:
# loop_tracker = LoopTracker([1, 2, 3])

# print(loop_tracker.first)
# print(next(loop_tracker))
# print()
# # TEST_8:
# loop_tracker = LoopTracker([])

# try:
#     print(loop_tracker.first)
# except AttributeError as e:
#     print(e)
# print()
# # TEST_9:
# loop_tracker = LoopTracker([1, 2, 3])

# print(next(loop_tracker))
# print(loop_tracker.last)
# print(next(loop_tracker))
# print(loop_tracker.last)
# print()
# # TEST_10:
# loop_tracker = LoopTracker([1, 2, 3])

# try:
#     print(loop_tracker.last)
# except AttributeError as e:
#     print(e)
# print()
# # TEST_11:
# loop_tracker = LoopTracker(range(1_000))

# for _ in range(100_000):
#     next(loop_tracker, None)

# print(loop_tracker.accesses)
# print(loop_tracker.empty_accesses)
# print()

# # TEST_13:
# loop_tracker = LoopTracker([1, 2, 3])

# try:
#     loop_tracker.accesses = 1
# except AttributeError as e:
#     print(type(e))

# try:
#     loop_tracker.first = 1
# except AttributeError as e:
#     print(type(e))

# try:
#     loop_tracker.last = 1
# except AttributeError as e:
#     print(type(e))