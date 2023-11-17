# Реализуйте функцию get_method_owner() , которая принимает два аргумента в
# следующем порядке:
    
# • cls — произвольный класс
# • method — строковое название метода

# Функция должна возвращать класс, от которого класс cls унаследовал
# метод method . Если метода method нет ни в самом классе, ни в одном другом
# классе из его иерархии, функция get_method_owner() должна вернуть
# значение None .


def get_method_owner(cls, method):
    for classes in cls.mro():
        if method in classes.__dict__:
            return classes
    return None    



# INPUT DATA:

# TEST_1:
class A:
    def m(self):
        pass
        
class B(A):
    pass

print(get_method_owner(B, 'm'))
print()
# TEST_2:
class A:
    def m(self):
        pass
        
class B(A):
    def m(self):
        pass

print(get_method_owner(B, 'm'))
print()
# TEST_3:
class A:
    pass
        
class B(A):
    pass

print(get_method_owner(B, 'm'))
print()
# TEST_4:
class Animal:
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return 'мяу'


class Kitten(Cat):
    pass


print(get_method_owner(Kitten, 'sound'))
print()
# TEST_5:
class A:
    def method(self):
        print('Метод класса A')


class B(A):
    def method(self):
        print('Метод класса B')


class C(A):
    def method(self):
        print('Метод класса C')


class D(B, C):
    pass


print(get_method_owner(D, 'method'))
print()
# TEST_6:
class A:
    def method(self):
        print('Метод класса A')


class B(A):
    pass


class C(A):
    def method(self):
        print('Метод класса C')


class D(B, C):
    pass


print(get_method_owner(D, 'method'))
print()
# TEST_7:
class A:
    def method(self):
        print('Метод класса A')


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(get_method_owner(D, 'method'))
print()
# TEST_8:
class A:
    def method(self):
        print('Метод класса A')


class B(A):
    def method(self):
        print('Метод класса B')


class C(A):
    def method(self):
        print('Метод класса C')


class D(B, C):
    def method(self):
        print('Метод класса D')


print(get_method_owner(D, 'method'))
print()
# TEST_9:
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(get_method_owner(D, 'method'))