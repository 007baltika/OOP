# С помощью множественного наследования постройте иерархию из приведенных
# ниже четырех классов. При решении старайтесь свести дублирование кода к
# минимуму.

class Father:
    
    def __init__(self, mood = 'neutral'):
        self.mood = mood
        
    def greet(self): return 'Hello!'
    def be_strict(self): self.mood = 'srtict'
    
class Mother(Father):
    
    def __init__(self, mood = 'neutral'):
        super().__init__(mood)
        
    def greet(self): return 'Hi, Honey!'
    def be_kind(self): self.mood = 'kind'
    
class Daughter(Mother, Father):
    
    def __init__(self, mood = 'neutral'):
        super().__init__(mood)
        
class Son(Father):
    
    def __init__(self, mood = 'neutral'):
        super().__init__(mood)  
        
    def be_kind(self): self.mood = 'kind'      
    
# INPUT DATA:

# TEST_1:
father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())
print()
# TEST_2:
father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)
print()
# TEST_3:
daughter = Daughter()

print(daughter.greet())
print(daughter.mood)
daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)
print()
# TEST_4:
son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)                       