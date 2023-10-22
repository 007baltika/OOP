# Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент: name — имя домашнего животного
# Экземпляр класса Pet должен иметь один атрибут: name — имя домашнего животного

# Класс Pet должен иметь три метода класса:

# first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
# last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
# num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet

class Pet:
    
    examples = []
    
    def __init__(self, name):
        self.name = name
        Pet.examples.append(self) # СОХРАНЯЕМ ЭКЗЕМПЛЯРЫ КЛАССА В ПЕРЕМЕННУЮ КЛАССА
    
    @classmethod    
    def first_pet(cls):
        if cls.examples == []: 
            return None
        else: return Pet.examples[0]  #ВЫВОДИМ ПЕРВЫЙ ЭЛЕМЕНТ В МАССИВЕ ВСЕХ ЭКЗЕМПЛЯРОВ, ПОЛУЧАЯ ДОСТУП БЛАГОДАРЯ Pet.переменная_класса[0]
    
    @classmethod    
    def last_pet(cls):
        if cls.examples == []: 
            return None
        else: return Pet.examples[-1]  
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.examples) 
            
 
 # TEST_1:
print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())
print()
# TEST_2:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
print()
# TEST_3:
names = ['Mia', 'Tutti', 'Erin', 'Loki', 'Kelly', 'Hussy', 'Abbey', 'Luna', 'Isha', 'Diva', 'Brandy', 'Petra', 'Mandy', 'Baby', 'Caitlyn', 'Taffy', 'Odie', 'Roxxy', 'Gabby', 'Shelby', 'Dolly', 'Ashley', 'Vanilla', 'Cori']

for name in names:
    pet = Pet(name)

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
print()
# TEST_4:
pet = Pet('Кемаль')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
print()
# TEST_5:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet4 = Pet('Ratchet')
pet5 = Pet('Ratchet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())       