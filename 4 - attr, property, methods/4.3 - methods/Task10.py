

class Numbers:
    
    def __init__(self):
        self.numbers = []
    
    def add_number(self, n):
        self.numbers.append(n)
        
    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))  
    
    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.numbers)) 
    
# INPUT DATA:

# TEST_1:
numbers = Numbers()

print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_2:
numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_3:
numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_4:
numbers = Numbers()

numbers.add_number(2)
numbers.add_number(2)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_5:
numbers = Numbers()

numbers.add_number(1)
numbers.add_number(2)
numbers.add_number(3)
numbers.add_number(4)

even = numbers.get_even()
odd = numbers.get_odd()
print(numbers.get_even())
print(numbers.get_odd())

even.append(None)
odd.append(None)
print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_6:
numbers = Numbers()

for n in range(1, 100, 2):
    numbers.add_number(n)

print(numbers.get_even())
print(numbers.get_odd())
print()
# TEST_7:
numbers = Numbers()

for n in range(0, 100, 2):
    numbers.add_number(n)

print(numbers.get_even())
print(numbers.get_odd())    