# Квадратный трехчлен — это многочлен вида ax^2 + bx + c 

# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# a — коэффициент квадратного трехчлена
# b — коэффициент квадратного трехчлена
# c — коэффициент  квадратного трехчлена
# Экземпляр класса QuadraticPolynomial должен иметь три атрибута: a, b, c
# Класс QuadraticPolynomial должен иметь два метода класса:

# from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c, которые представляют коэффициенты квадратного трехчлена, 
# и возвращающий экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов

# from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c квадратного трехчлена, записанные через пробел. 
# Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float 

class QuadraticPolynomial:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @classmethod    
    def from_iterable(cls, mass_abc):
        new_a, new_b, new_c = mass_abc
        return cls(new_a, new_b, new_c)
    
    @classmethod
    def from_str(cls, string_abc):
        new_a, new_b, new_c = map(lambda num: float(num), string_abc.split())
        return cls(new_a, new_b, new_c)
    
# TEST_1:
polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)
print()
# TEST_2:
polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)
print()
# TEST_3:
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
print()
# TEST_4:
polynom = QuadraticPolynomial.from_str('-19 40 148')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print()
# TEST_5:
polynom = QuadraticPolynomial.from_iterable([25, 132, -18])

print(polynom.a)
print(polynom.b)
print(polynom.c)
print()
# TEST_6:
polynom = QuadraticPolynomial.from_iterable([2.5, 13.2, -1.8])

print(polynom.a)
print(polynom.b)
print(polynom.c)    