# Требовалось реализовать класс Item , описывающий предмет. При создании
# экземпляра класс должен был принимать три аргумента в следующем порядке:
# • name — название предмета
# • price — цена предмета в рублях
# • quantity — количество предметов
# Предполагалось, что при обращении к атрибуту name экземпляра
# класса Item будет возвращаться его название с заглавной буквы, а при
# обращении к атрибуту total — произведение цены предмета на его количество.
# Программист торопился и решил задачу неправильно. 

class Item:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __getattribute__(self, attr):
        if attr == 'name': 
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        if attr == 'total': 
            return self.price * self.quantity

        

# TEST_1:
fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)
print()
# TEST_2:
fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)
print()
# TEST_3:
course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)
print()
# TEST_4:
items = [
    Item('Обручальное Кольцо', 49000, 7),
    Item('Мобильный Телефон', 110000, 200),
    Item('Ноутбук', 150000, 2000),
    Item('Ручка Паркер', 37000, 20),
    Item('Статуэтка Оскар', 28000, 4000),
    Item('Наушники', 11000, 150),
    Item('Гитара', 32000, 1500),
    Item('Золотая Монета', 140000, 8),
    Item('Фотоаппарат', 79000, 720),
    Item('Лимитированные Кроссовки', 80000, 300)
]

for item in items:
    print(item.name, item.total)
print()
# TEST_5:
goods = [
    Item('Морковь', 257, 20),
    Item('Лук', 251, 10),
    Item('Свекла', 120, 11),
    Item('Капуста', 280, 2),
    Item('Огурцы', 87, 5),
    Item('Помидоры', 123, 3),
    Item('Болгарский', 192, 2),
    Item('Перец', 197, 9),
    Item('Яблоки', 261, 3),
    Item('Груши', 103, 15),
    Item('Лимон', 166, 7),
    Item('Апельсины', 213, 2),
    Item('Бананы', 71, 13),
    Item('Виноград', 247, 10),
    Item('Киви', 226, 20)
]

for product in goods:
    print(product.name, product.total, 'руб.')        