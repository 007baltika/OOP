# Реализуйте класс Closer . При создании экземпляра класс должен принимать
# один аргумент:
# • obj — произвольный объект
# Экземпляр класса Closer должен являться контекстным менеджером, который
# закрывает используемый объект obj с помощью метода close() после
# выполнения кода внутри блока with . Если объект не поддерживает операцию
# закрытия, контекстный менеджер должен вывести:
# Незакрываемый объект

class Closer:
    
    def __init__(self, obj):
        self.obj = obj
        
    def __enter__(self):
        return self.obj
    
    def __exit__(self, *args, **kwargs):
        try:
            self.obj.close()
        except Exception:
            print("Незакрываемый объект")
        return True    
    
# TEST_1:
output = open('output.txt', 'w', encoding='utf-8')

with Closer(output) as file:
    print(file.closed)
    
print(file.closed)
print()
# TEST_2:
with Closer(5) as i:
    i += 1
    
print(i)
print()
# TEST_3:
from zipfile import ZipFile

zip_file = ZipFile('test.zip', 'w')

with Closer(zip_file) as zf:
    print(zf)
print()
# TEST_4:
unclosable = [3.14, 'Elon', {'Ч': 'LXXIV'}, [1, 2, 3], (4, 5, 6), True, False]

for item in unclosable:
    with Closer(item) as zf:
        print(item)          