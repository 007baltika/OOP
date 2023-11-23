
# Реализуйте класс Queue , описывающий очередь, элементами которой являются
# пары ключ: значение . При создании экземпляра класс должен принимать один
# аргумент:

# • pairs — список или словарь, определяющий начальный набор элементов
# очереди. Порядок элементов в очереди должен совпадать с их порядком в
# переданном итерируемом объекте. Если не передан, очередь считается
# пустой

# Класс Queue должен иметь два метода экземпляра:

# • add() — метод, принимающий в качестве аргумента элемент и
# добавляющий его в конец очереди. Элементом в данном случае является
# двухэлементный кортеж, содержащий ключ и значение. Если в очереди уже
# содержится элемент с указанным ключом, он должен быть перенесен в
# конец очереди, а его значение должно быть обновлено

# • pop() — метод, удаляющий из очереди первый элемент и возвращающий
# его. Элементом в данном случае является двухэлементный кортеж,
# содержащий ключ и значение. Если очередь пуста, должно быть
# возбуждено исключение KeyError с текстом: 'Очередь пуста'

# Экземпляр класса Queue должен иметь следующее формальное строковое
# представление: Queue([(<ключ 1-го элемента>, <значение 1-го элемента>), (<ключ 2-го элемента>, <значение 2-го элемента>), ...])

# При передаче экземпляра класса Queue в функцию len() должно возвращаться количество элементов в нем.

from collections import UserDict, UserList



class List(UserList):
    pass

class Dict(UserDict):
    pass


class Queue():
    
    def __init__(self, pairs=[]):
        # Если на вход поступил словарь, то создаю переменную, которая является экземпляром класса Dict - UserDict и потом уже оперирую им как словарем
        if isinstance(pairs, dict):
            self.pairs = Dict(pairs)
        # Если на вход поступил список, то создаю переменную, которая является экземпляром класса List - UserList и потом уже оперирую им как списком    
        else:
            self.pairs = List(pairs)
        
    def add(self, element):
        if isinstance(self.pairs, Dict):
           if element[0] not in self.pairs.keys():
                self.pairs[element[0]] = element[1]
           else:
               # ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СЛОВАРЬ - В КОНЕЦ, А СТАРОЕ - ЗАТЕРЕТЬ
                for key, value in self.pairs:
                    if key == element[0]:
                        del self.pairs[key]
                self.pairs[element[0]] = element[1] 
            
        else:
            for pair in self.pairs:
                if pair[0] == element[0]:
                    self.pairs.remove(pair)
            self.pairs.append(element)    
                
    def pop(self):
        # Работает только со списком, но по условию и не требовалось чтобы работало со словарем
        if len(self.pairs) != 0: 
            return self.pairs.pop(0)                   
        else: raise KeyError("Очередь пуста")
            
    def __len__(self): return len(self.pairs)
    
    def __repr__(self):
        return f'Queue({self.pairs})'
    
            

    
# INPUT DATA:

# TEST_1:
queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)
print()
# TEST_2:
queue = Queue([('one', 1)])

queue.add(('two', 2))
print(queue.pop())
print(queue.pop())
print(queue)
print()
# TEST_3:
queue = Queue({'one': 1, 'two': 2})

print(len(queue))
queue.add(('three', 1))
print(len(queue))
print()
# TEST_4:
queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)
queue.add(('one', 10))
print(queue)
print()
# TEST_5:
queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)
print()
# TEST_6:
data = [('Kerry Martinez', 36), ('Todd Watson', 47), ('Andrew Elliott', 56), ('Jamie Collins', 44),
        ('Kelli Aguilar', 35), ('Sara Guerrero', 20), ('Michelle Allen', 29), ('Elizabeth George', 17),
        ('Suzanne Rodriguez', 42), ('Timothy Smith', 46), ('Dr. Olivia Thomas', 59), ('Kevin Johnson', 59),
        ('Jennifer Padilla', 54), ('Ariel Saunders', 26), ('Jason Haley', 28), ('David Howard', 20),
        ('Duane Dixon', 57), ('Sierra Graves', 30), ('Todd Watson', 46), ('Amanda Wilson', 45), ('Nicole Johnson', 24),
        ('Lauren Lopez', 25), ('Amanda Miranda', 30), ('Sharon Russell', 29), ('Robert Richardson', 40),
        ('Kristen Thompson', 32), ('Adam Bush', 33), ('Mackenzie Hanson', 50), ('David Ortega', 48),
        ('Tim Williams', 29), ('Angela Johnson', 41), ('Duane Watson', 31), ('Tamara Wood', 13), ('Julie Morris', 40),
        ('Michele Blake', 52), ('Kevin Hill', 28), ('Wesley Roberts', 14), ('Autumn Ryan', 15), ('Jeff Cline', 36),
        ('Timothy Taylor', 34), ('Yolanda Morris', 34), ('Christina Johnson', 43), ('Shaun Johnson', 48),
        ('Elizabeth Lopez', 31), ('Angela Ramos', 47), ('Andrea Roberts', 20), ('Carrie Santiago', 16),
        ('Valerie Hunt', 18), ('Jasmin May', 31), ('Ethan Smith', 57), ('Cynthia Miles', 32), ('Thomas Johnson', 19),
        ('Brenda Ochoa', 39), ('Tammy Shields', 16), ('Jodi Combs', 17), ('Edward Evans', 50), ('Susan Maldonado', 49),
        ('Kelly Harris', 43), ('Dawn Graham', 32), ('Cynthia Simpson', 35), ('James Norris', 58),
        ('Jeanne Blevins', 26), ('Bradley Hall', 39), ('Bridget Holland', 22), ('Paul Henderson', 47),
        ('James Stein', 24), ('Joshua Moore', 44), ('Aaron Chandler', 48), ('Jason Vance', 18), ('David Williams', 48),
        ('Donna Johnson', 45), ('Shelby Schmidt', 25), ('Cody Ford', 35), ('William Hampton', 41),
        ('Michael Cooper', 20), ('Megan Snyder', 34), ('Wendy Baxter', 47), ('Nicole Walker', 16), ('Kelly Harris', 57),
        ('Maurice Brady', 58), ('Jennifer Mayo', 26), ('Cynthia Miles', 43), ('Michelle Conley', 38),
        ('Andrew Gonzalez', 10), ('Christina Grant', 53), ('Jessica Pena', 22), ('Jerry Carroll', 16),
        ('Candace Aguirre', 49), ('Curtis Hall', 20), ('Adam Bush', 46), ('Carrie Williams', 26), ('Lisa Barker', 27),
        ('Thomas Smith', 36), ('Sheila Marsh PhD', 55), ('Tracy Potts', 23), ('Christopher Brown', 46),
        ('Michael Thompson', 47), ('Jennifer Peterson MD', 15), ('Paul Henderson', 24), ('Julie Gibson', 48)]

queue = Queue([('Allison Finley', 14), ('Bryan Bradshaw', 48)])

for item in data:
    queue.add(item)

print(len(queue))
for _ in range(97):
    print(queue.pop())

try:
    queue.pop()
except KeyError as e:
    print(e)

print(len(queue))    