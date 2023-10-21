from math import sqrt

class QuadraticPolynomial:
    
    def __init__(self, a, b , c):
        self.a = a
        self.b = b
        self.c = c
        
    @property
    def x1(self):
        d = pow(self.b, 2) - 4 * self.a * self.c
        if d < 0: self._x1 = None
        else: self._x1 = (- self.b - sqrt(d) ) / (2 * self.a)
        return self._x1   
    
    @property
    def x2(self):
        d = pow(self.b, 2) - 4 * self.a * self.c
        if d < 0: self._x2 = None
        else: self._x2 = (- self.b + sqrt(d) ) / (2 * self.a)
        return self._x2 
    
    @property
    def view(self):
        list_things = [self.b, self.c]
        string = [a for a in map(lambda chislo: '- ' + str(abs(chislo)) if chislo < 0 else '+ ' + str(chislo), list_things)]
        return f'{self.a}x^2 {string[0]}x {string[1]}'
    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, new_coefficients):
        self.a, self.b, self.c = new_coefficients
    
# INPUT DATA:

# TEST_1:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)
print()
# TEST_2:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)
print()
# TEST_3:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)
print()
# TEST_4:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print()
# TEST_5:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print()
# TEST_6:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print()
# TEST_7:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print()
# TEST_8:
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)
print()
# TEST_9:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)   