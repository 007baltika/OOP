# Коды состояния HTTP представляют собой трехзначные целые числа и
# используются для указания успешности конкретного HTTP запроса. Выделяют
# пять групп кодов состояния:
# • информация ( 100-199 )
# • успех ( 200-299 )
# • перенаправление ( 300-399 )
# • ошибка клиента ( 400-499 )
# • ошибка сервера ( 500-599 )

# Реализуйте класс HTTPStatusCodes , описывающий перечисление с кодами
# состояния HTTP. Перечисление должно иметь пять элементов:
# • CONTINUE — элемент со значением 100
# • OK — элемент со значением 200
# • USE_PROXY — элемент со значением 305
# • NOT_FOUND — элемент со значением 404
# • BAD_GATEWAY — элемент со значением 502

# Элемент перечисления должен иметь два метода:
# • info() — метод, возвращающий двухэлементный кортеж, содержащий
# имя элемента и его значение
# • code_class() — метод, возвращающий название группы на русском, к
# которой относится элемент



from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502
    
    def info(self):
        return (self.name, self.value)
    
    def code_class(self):
        if self.value in range(100, 200):
            return f'информация'
        elif self.value in range(200, 300):
            return f'успех'
        elif self.value in range(300, 400):
            return f'перенаправление'
        elif self.value in range(400, 500):
            return f'ошибка клиента'
        elif self.value in range(500, 600):
            return f'ошибка сервера'
            



# INPUT DATA:

# TEST_1:
print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())
print()
# TEST_2:
print(HTTPStatusCodes.CONTINUE.info())
print(HTTPStatusCodes.CONTINUE.code_class())
print()
# TEST_3:
print(HTTPStatusCodes.USE_PROXY.info())
print(HTTPStatusCodes.USE_PROXY.code_class())
print()
# TEST_4:
print(HTTPStatusCodes.NOT_FOUND.info())
print(HTTPStatusCodes.NOT_FOUND.code_class())
print()
# TEST_5:
print(HTTPStatusCodes.BAD_GATEWAY.info())
print(HTTPStatusCodes.BAD_GATEWAY.code_class())
print()
# TEST_6:
for instance in HTTPStatusCodes:
    print(f'{instance.name} -> {instance.value}')          