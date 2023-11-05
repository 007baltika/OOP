# Реализуйте класс Suppress . При создании экземпляра класс должен принимать
# произвольное количество позиционных аргументов, каждый из которых
# представляет собой тип исключения.
# Экземпляр класса Suppress должен являться контекстным менеджером,
# подавляющим исключение, если оно возбуждается во время выполнения кода
# внутри блока with . Подавляться должны исключения тех типов, которые были
# перечислены при создании контекстного менеджера.

# Также экземпляр класса Suppress должен иметь один атрибут:
# • exception — исключение, которое было подавлено контекстным

# менеджером. Если исключение не было подавлено или код был выполнен
# без исключений, атрибут должен иметь значение None


class Suppress:
    
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        for error in self.exceptions:
            if exc_type == error:
                self.exception = exc_value
                return True
        return False       
    
# INPUT DATA:

# TEST_1:
with Suppress(NameError):
    print('Этой переменной не существует -->', variable)
    
print('Завершение программы')
print()
# TEST_2:
with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))
print()
# TEST_3:
with Suppress() as context:
    print('All success!')

print(context.exception)
print()
# TEST_4:
with Suppress(ValueError) as context:
    try:
        number = list(123)
    except TypeError:
        pass

print(context.exception)
print()
# TEST_5:
iterable = iter(range(100))

with Suppress(StopIteration) as context:
    for _ in range(99):
        next(iterable)
    print(next(iterable))
    print(next(iterable))


print(context.exception)
print(type(context.exception))
print()
# TEST_6:
d = {'Gvido': 67, 'Gates': 67, 'Zuckerberg': 38}
with Suppress(KeyError) as context:
    print(d['Mask'])


print(context.exception)
print(type(context.exception))
print()
# TEST_7:
with Suppress(ValueError) as context:
    try:
        print('Несуществующий метод у словаря –>', {}.new())
    except AttributeError as e:
        print(type(e))

print(context.exception)
print()
# TEST_8:
try:
    with Suppress(ValueError) as context:
        number = list(123)
except TypeError:
    pass

print(context.exception)
                