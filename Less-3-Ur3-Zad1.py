# Программа должна складывать вектора с числами, а также с другими веторами. Если сложение с другим типом данных, программа вызывает ошибку

# Например:
# v1 = Vector(1,2,3)
# v2 = Vector(3,4,5)
# v3 = v1 + v2
# print(v3) = Вектор(4, 6, 8)
# v4 = v3 + 5
# print(v4) = Вектор(9, 11, 13)
# v5 = v1 * 2
# print(v5) = Вектор(2, 4, 6)
# v5 + "hi" = нельзя сложить с 'hi'    

class Vector():
    
    def __init__(self, *kwargs):
        self.values = list(kwargs)
        self.values.sort()
                
    def __str__(self):
        if len(self.values) > 0: 
            mass_nums_as_str = []
            for i in range(0, len(self.values)):
                mass_nums_as_str.append(str(self.values[i]))
            return f'Вектор({", ".join(mass_nums_as_str)})'    
        else: return "Пустой вектор" 
        
    def __add__(self, num_for_summ):
        #Если это число - работает
        if isinstance(num_for_summ, int):
            mass_for_summ_nums = []
            for k in range(0, len(self.values)):
                mass_for_summ_nums.append(self.values[k] + num_for_summ)
            return Vector(*mass_for_summ_nums)
        #Если это вектор - надо чтобы новый созданный вектор снова проинициализировался, тк у него не сохраняется переменная values
        if isinstance(num_for_summ, Vector):
            mass_for_summ_vectors = []
            if len(self.values) == len(num_for_summ.values):
                for j in range(0, len(self.values)):
                    mass_for_summ_vectors.append(self.values[j] + num_for_summ.values[j]) 
                return Vector(*mass_for_summ_vectors)            
            else: return 'Сложение векторов разной длины недопустимо'
        
        if not isinstance(num_for_summ, (int, Vector)): return f'Вектор нельзя сложить с {num_for_summ}'
        
    def __mul__(self, num_for_mul):
        #Если число - работает   
        if isinstance(num_for_mul, int):
            mass_for_mul_nums = []
            for l in range(0, len(self.values)):
                mass_for_mul_nums.append(self.values[l] * num_for_mul)
            return Vector(*mass_for_mul_nums)
        #Если это вектор                           
        if isinstance(num_for_mul, Vector):
            mass_for_mul_vectors = []
            if len(self.values) == len(num_for_mul.values):
                for m in range(0, len(self.values)):
                    mass_for_mul_vectors.append(self.values[m] * num_for_mul.values[m])
                return Vector(*mass_for_mul_vectors)        
            else: return 'Умножение векторов разной длины недопустимо'
        
        if not isinstance(num_for_mul, (int, Vector)): return f'Вектор нельзя умножать с{num_for_mul}'    
        
Console.ReadLine()         