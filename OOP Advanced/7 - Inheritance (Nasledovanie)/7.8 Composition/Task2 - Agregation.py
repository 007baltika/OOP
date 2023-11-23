

# 1. Реализуйте класс Item , описывающий товар. При создании экземпляра класс
# должен принимать два аргумента в следующем порядке:
# • name — название товара
# • price — цена товара в долларах
# Экземпляр класса Item должен иметь следующее неформальное строковое
# представление:
# <название товара>, <цена товара>$

# 2. Также реализуйте класс ShoppingCart , описывающий корзину для покупок.
# При создании экземпляра класс должен принимать один аргумент:
# • items — итерируемый объект, определяющий начальный набор
# товаров в корзине. Если не передан, корзина считается пустой
# Класс ShoppingCart должен иметь три метода экземпляра:
# • add() — метод, принимающий в качестве аргумента товар и
# добавляющий его в корзину
# • total() — метод, возвращающий суммарную стоимость всех товаров в
# корзине
# • remove() — метод, принимающий в качестве аргумента название товара
# и удаляющий его из корзины. Если в корзине несколько товаров с
# указанным именем, они должны быть удалены все

# Экземпляр класса ShoppingCart должен иметь следующее неформальное
# строковое представление:
# <название первого товара в корзине>, <цена первого товара в корзине>$
# <название второго товара в корзине>, <цена второго товара в корзине>$
# ...............


from functools import reduce

class Item:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f'{self.name}, {self.price}$'
    
class ShoppingCart:
    
    def __init__(self, items=[]):
        # items у нас экземпляр класса Item, т.е. мы можем через self.items.name и self.items.price получать название и цену товара
        self.items = items 
        
    def add(self, obj):
        self.items.append(obj)
        
    def total(self):
        summ = 0
        for item in self.items:
            summ += item.price
        return summ
    
    def remove(self, item_for_del):
        for item in self.items:
            if item.name == item_for_del:
                self.items.remove(item)  
                
    def __str__(self):
        st = []
        for item in self.items:
            st.append(f'{item.name}, {item.price}$') 
        return '\n'.join(st) 
    



# INPUT DATA:

# TEST_1:
item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)
print()
# TEST_2:
shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())
print()
# TEST_3:
shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())
print()
# TEST_4:
shopping_cart = ShoppingCart([Item('Banana', 100), Item('Apple', 120), Item('Orange', 110), Item('Tomato', 180), Item('Cucumber', 150)])

shopping_cart.add(Item('Banana', 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove('Banana')
print(shopping_cart)
print(shopping_cart.total())
print()
# TEST_5:
shopping_cart = ShoppingCart()
print(shopping_cart)                    