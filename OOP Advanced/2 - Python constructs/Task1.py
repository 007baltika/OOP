# Задание
# Будем считать, что игровое поле для игры в дартс представляет собой
# квадратную матрицу, заполненную натуральными числами, расположенными в
# порядке возрастания от краев к центру. Стороной игрового поля будем называть
# сторону квадратной матрицы, которую представляет это поле.
# Напишите программу, которая создает поле для игры в дартс определенного
# размера.


n = int(input())

if n % 2 == 0:
    
    otvet = []
    centr = n // 2
    
    for num_stroki in range(1, (n // 2) + 1):
        
        stroka = []
       
        for chisla_v_stroke in range(1, (n // 2) + 1):
            
            if chisla_v_stroke > num_stroki: 
                stroka.append(num_stroki)
            else: stroka.append(chisla_v_stroke)
      
        otvet.append(stroka + stroka[::-1]) 
    
    [print(*st, end = '\n') for st in (otvet + otvet[-1::-1])]      

if n % 2 == 1:
    
    otvet = []
    centr = n // 2
    
    for num_stroki in range(1, (n // 2) + 2):
        
        stroka = []
                
        for chisla_v_stroke in range(1, (n // 2) + 2):
            
            if chisla_v_stroke > num_stroki: 
                stroka.append(num_stroki)
            else: stroka.append(chisla_v_stroke)
                
        otvet.append(stroka + stroka[-2::-1])
            
    [print(*st, end = '\n') for st in (otvet + otvet[-2::-1])] 

# TEST_1: n = 1
# 1

# TEST_2: n = 2
# 1 1
# 1 1

# TEST_3: n = 3
# 1 1 1
# 1 2 1
# 1 1 1

# TEST_4: n = 4
# 1 1 1 1
# 1 2 2 1
# 1 2 2 1
# 1 1 1 1

# TEST_5: n = 5
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

# TEST_6: n = 6
# 1 1 1 1 1 1
# 1 2 2 2 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 2 2 2 1
# 1 1 1 1 1 1   

# TEST_7: n = 7
# 1 1 1 1 1 1 1
# 1 2 2 2 2 2 1
# 1 2 3 3 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 3 3 2 1
# 1 2 2 2 2 2 1
# 1 1 1 1 1 1 1         