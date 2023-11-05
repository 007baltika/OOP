# Реализуйте класс WriteSpy . При создании экземпляра класс должен принимать
# три аргумента в следующем порядке:
    
# • file1 — файловый объект
# • file2 — файловый объект
# • to_close — булево значение, по умолчанию равняется false
# Экземпляр класса WriteSpy должен являться контекстным менеджером,
# который выполняет операцию записи сразу в оба файловых
# объекта file1 и file2 . Параметр to_close должен определять состояние
# файловых объектов file1 и file2 после завершения блока with . Если
# он имеет значение true , после завершения блока with контекстный менеджер
# должен закрыть оба файловых объекта, если false — оставить открытыми.
# Класс WriteSpy должен иметь четыре метода экземпляра:
# • write() — метод, принимающий в качестве аргумента текст и
# записывающий его в оба файловых объекта. Если хотя бы один из
# файловых объектов закрыт или недоступен для записи, должно быть
# возбуждено исключение ValueError с текстом:
# Файл закрыт или недоступен для записи
# • close() — метод, немедленно закрывающий оба файловых объекта
# • writable() — метод, возвращающий true , если оба файловых объекта
# доступны для записи, или false в противном случае
# • closed() — метод, возвращающий true , если оба файловых объекта
# закрыты, или false в противном случае


class WriteSpy:
    
    def __init__(self, file1, file2, to_close = False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close
        
        
    def write(self, text):
        if self.file1.closed == False and self.file2.closed == False:
            if self.file1.writable() and self.file2.writable():
                self.file1.write(text)
                self.file2.write(text)
            else: raise ValueError("Файл закрыт или недоступен для записи")    
        else: raise ValueError("Файл закрыт или недоступен для записи")
    
    def close(self):
        self.file1.close()
        self.file2.close()
    
    def writable(self):
        if self.file1.closed == False and self.file2.closed == False:
            if self.file1.writable() and self.file2.writable():
                return True
            else: return False
        else: return False
    
    def closed(self):
        if self.file1.closed == True and self.file2.closed == True:
            return True
        else: return False
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close == True: 
            self.close()
        return False    
    
    
    
    
# TEST_1:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())
print()
# TEST_2:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())
    
f1 = open('file1.txt')
f2 = open('file2.txt')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())
print()
# TEST_3:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())
print()
# TEST_4:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=False) as combined:
    print(f1.closed, f2.closed)
    combined.close()
    print(f1.closed, f2.closed)
print()
# TEST_5:
f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)
print()
# TEST_6:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)
print()
# TEST_7:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())
print()
# TEST_8:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    pass

print(combined.closed())
print()
# TEST_9:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2) as combined:
    pass

print(combined.closed())  
            