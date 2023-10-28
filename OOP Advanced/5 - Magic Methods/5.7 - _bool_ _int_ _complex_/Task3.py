
#желательно деделать, успешно на 70%

from functools import total_ordering

@total_ordering
class RomanNumeral:
    
    def __init__(self, number):
        
        if isinstance(number, str):
            rim_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            des = 0
            ostatki_for_sub = 0
            
            if len(number) > 1:
                for i in range(0, len(number) - 1):

                    if rim_dict[number[i]] <= rim_dict[number[i+1]]: 
                        ostatki_for_sub += rim_dict[number[i]]
                        continue
                    elif ostatki_for_sub != 0 and rim_dict[number[i]] > rim_dict[number[i-1]]:
                        vichit = rim_dict[number[i]] - ostatki_for_sub
                        ostatki_for_sub = 0
                        des += vichit
                    else: des += rim_dict[number[i]]   

                des += ostatki_for_sub + rim_dict[number[-1]]   
                print(des)
                self.rim = des 
            
            else: self.rim = rim_dict[number]
            
        else: self.rim = number
        
    def __str__(self):
        return f'{self.rim}'
    
    def __int__(self):
        return int(self.rim) 
    
    def __eq__(self, other_examp):
        if isinstance(other_examp, RomanNumeral): return self.rim == other_examp.rim
        return NotImplemented
    
    def __lt__(self, other_examp):
        if isinstance(other_examp, RomanNumeral): return self.rim < other_examp.rim
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, RomanNumeral): 
            return RomanNumeral(self.rim + other.rim)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, RomanNumeral): 
            return RomanNumeral(self.rim - other.rim)
        return NotImplemented

# TEST_1:
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))
print()
# TEST_2:
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))
print()
# TEST_3:
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print()
# TEST_4:
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print()
# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))
print()
# TEST_6:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V') 

print(number)
print(int(number))
print()
# TEST_7:
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))
print()
# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))
print()
# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))
print()
# TEST_10:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))            