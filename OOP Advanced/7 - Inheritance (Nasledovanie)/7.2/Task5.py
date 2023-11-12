

class Summator:
    
    stepen = 1
    
    def total(self, n):
        # return sum(range(1, n+1))
        return sum(map(lambda x: pow(x, Summator.stepen), [num for num in range(1, n+1)])) 
    
    
class SquareSummator(Summator):
        
    def total(self, n):
        Summator.stepen = 2
        return Summator.total(self, n)
        # return sum(map(lambda x: pow(x, 2), [num for num in range(1, n+1)])) 
    
    
class QubeSummator(Summator):
    
    def total(self, n):
        Summator.stepen = 3
        return Summator.total(self, n)
        # return sum(map(lambda x: pow(x, 3), [num for num in range(1, n+1)]))     
    
    
class CustomSummator(Summator):
    
    def __init__(self, m):
        self.stepen = m
    
    def total(self, n):
        Summator.stepen = self.stepen
        return Summator.total(self, n)
        # return sum(map(lambda x: pow(x, self.stepen), [num for num in range(1, n+1)])) 
    


# INPUT DATA:

# TEST_1:
print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))
print()
# TEST_2:
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
print()
TEST_3:
summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
print()
# TEST_4:
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

for i in range(5, 50):
    print(summator1.total(i), summator2.total(i), summator3.total(i))
print()
# TEST_5:
for i in range(5, 50):
    summator = CustomSummator(i)
    print(summator.total(10))        
    