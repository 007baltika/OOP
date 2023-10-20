

class Todo:
    
    def __init__(self):
        self.things = []
        self.get_low = []
        self.get_max = []
        
    def add(self, thing, priority):
        self.things.append([thing, priority])
        
    def get_by_priority(self, n):
        get_priority_n = []
        for thing in self.things:
            if thing[1] == n:
                get_priority_n.append(thing[0])
        return get_priority_n
    
    def get_low_priority(self):
        if self.things != []:
            min_priority = min(self.things, key = lambda thing: thing[1])
            for thing in self.things:
                if thing[1] == min_priority[1]:
                   self.get_low.append(thing[0])
        return self.get_low   
    
    def get_high_priority(self):
        
        if self.things != []:
            max_priority = max(self.things, key = lambda thing: thing[1])
            for thing in self.things:
                if thing[1] == max_priority[1]:
                    self.get_max.append(thing[0])
        return self.get_max       
    
    
# INPUT DATA:

# TEST_1:
todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())
print()

# TEST_2:
todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))
print()
# TEST_3:
todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
print()
# TEST_4:
todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())    