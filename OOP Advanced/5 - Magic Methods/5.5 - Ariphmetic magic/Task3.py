

class SuperString:
    
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        return self.string 
    
    def __add__(self, other):
        if isinstance(other, SuperString): return SuperString(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int): return SuperString(self.string * n)
        return NotImplemented   
    
    def __rmul__(self, n):
        if isinstance(n, int): return self.__mul__(n)
        return NotImplemented   
    
    def __truediv__(self, n):
        if isinstance(n, int): 
            m = len(self.string) // n
            return SuperString(self.string[0:m])
        return NotImplemented  
    
    def __lshift__(self, n):
        if isinstance(n, int): return SuperString(self.string[:n])
        return NotImplemented  
    
    def __rshift__(self, n):
        if isinstance(n, int): return SuperString(self.string[n:])
        return NotImplemented  
    
# TEST_1:
s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)
print()
# TEST_2:
s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)
print()
# TEST_3:
s = SuperString('beegeek')

print(s << 4)
print(s >> 3)
print()
# TEST_4:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)
print()
# TEST_5:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} >> {i} =', s >> i)
print()
# TEST_6:
names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон', 'Добромысл',
         'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир', 'Орест',
         'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен', 'Велимир',
         'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
         'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
         'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан', 'Гордей',
         'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
         'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
         'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
         'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

for name in names:
    person = SuperString(name)
    print(person * 2, 2 * person, person / 2)
print()
# TEST_7:
s = SuperString('beegeek')
for i in range(1, 9):
    print(f'{s} / {i} =', s / i)
print()
# TEST_8:
superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))
print()
# TEST_9:
s1 = SuperString('bee')
s2 = SuperString('geek')

new_s1 = s1 << 1
new_s2 = s2 >> 1
new_s3 = s1 + s2
new_s4 = s1 * 2
new_s5 = s2 / 2

print(new_s1, type(new_s1))
print(new_s2, type(new_s2))
print(new_s3, type(new_s3))
print(new_s4, type(new_s4))
print(new_s5, type(new_s5))    