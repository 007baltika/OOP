# Реализуйте класс RoundedInt , наследника класса int , описывающий целое
# число, которое во время создания автоматически округляется до ближайшего
# четного или нечетного числа. При создании экземпляра класс должен принимать
# два аргумента в следующем порядке:
# • num — объект, определяющий числовое значение экземпляра
# класса RoundedInt
# • even — булево значение, определяющее четность при округлении. Если
# имеет значение true , округление происходит до ближайшего четного,
# если false — до ближайшего нечетного. По умолчанию имеет
# значение true

class RoundedInt(int):
    
    def __new__(cls, num, even = True):
        if even == True:
            if num % 2 == 0:
                num = num
            else:
                if (num + 1) % 2 == 0:
                    num = num + 1
                else: num = num - 1        
            instance = super().__new__(cls, num)
            return instance
        elif even == False:
            if num % 2 == 1:
                num = num
            else:
                if (num + 1) % 2 == 1:
                    num = num + 1
                else: num = num - 1  
            instance = super().__new__(cls, num)
            return instance   
        
# INPUT DATA:

# TEST_1:
print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))
print()
# TEST_2:
roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
print()
# TEST_3:
print(issubclass(RoundedInt, int))
print()
# TEST_4:
for digit in range(100):
    print(RoundedInt(digit))
print()
# TEST_5:
for digit in range(100):
    print(RoundedInt(digit, False))        