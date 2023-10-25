


import numpy as np

class Matrix:
    
    def __init__(self, rows, cols, value = 0):
        self.rows = rows
        self.cols = cols
        if type(value) == int:
            self.value = value
            self.matrix = []
            for row in range(self.rows):
                self.matrix += [self.cols * [value]]
        else:
            self.matrix = value        
        
    def get_value(self, row, col):
        return self.matrix[row][col]
    
    def set_value(self, row, col, value):
        self.matrix[row][col] = value
        return self.matrix
    
    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})' 
    
    def __str__(self):
        return '\n'.join([' '.join(str(a) for a in znach) for znach in self.matrix])
                
    def __pos__(self):
        return Matrix(self.rows, self.cols, self.value)  
    
    def __neg__(self):
        neg_matrix = []
        for row in self.matrix:
            neg_matrix += [[-a for a in row]]
        return Matrix(self.rows, self.cols, neg_matrix) 
    
    def __invert__(self):
        matr_array = np.array(self.matrix)
        transponse = np.transpose(matr_array)
        return Matrix(self.rows, self.cols, transponse)
    
    def __round__(self, n = None):
        round_matrix = []
        for row in self.matrix:
            round_matrix += [[round(a, n) for a in row]]
        return Matrix(self.rows, self.cols, round_matrix)       
    
# TEST_1:
print(Matrix(2, 3))
print()
# TEST_2:
matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)
print()
# TEST_3:
matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)
print()
# TEST_4:
matrix = Matrix(2, 3)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))

matrix.set_value(0, 0, 100)
matrix.set_value(1, 1, 200)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))
print()
# TEST_5:
matrix = Matrix(4, 2)

counter = 1
for row in range(4):
    for col in range(2):
        matrix.set_value(row, col, counter)
        counter += 1

print(matrix)
print()
print(~matrix)
print()
# TEST_6:
matrix1 = Matrix(4, 2)
matrix2 = Matrix(10, 20, value=6)

print(repr(matrix1))
print(repr(matrix2))
print()
# TEST_7:
matrix = Matrix(5, 10)

floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
           -3087.5496014, 3861.68814],
          [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
           -8949.9313078, -7032.4347679, -5217.8236385],
          [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
           -9484.68116, 639.6343972, 3444.9938213],
          [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
           4370.9173164, -8851.7648474, 8990.6896422],
          [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
           8531.2015615, -244.3630074, 3421.8817151]]

for r in range(5):
    for c in range(10):
        matrix.set_value(r, c, floats[r][c])

print(matrix)
print()
print(~matrix)
print()
print(round(matrix, 2))
print()
print(-matrix)
print()
# TEST_8:
matrix = Matrix(2, 3, 1)

round_matrix = round(matrix)
plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(round_matrix is matrix)
print(plus_matrix is matrix)
print(minus_matrix is matrix)
print(invert_matrix is matrix)
print()
# TEST_9:
matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)          