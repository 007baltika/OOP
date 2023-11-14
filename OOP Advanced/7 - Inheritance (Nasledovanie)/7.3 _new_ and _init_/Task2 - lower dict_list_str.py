# Реализуйте класс LowerString , наследника класса str , описывающий строку,
# которая во время создания автоматически переводится в нижний регистр. При
# создании экземпляра класс должен принимать один аргумент:
    
# • obj — объект, определяющий начальное значение строки. Может быть не
# передан, в таком случае начальное значение считается пустой строкой



class LowerString(str):
    
    def __new__(cls, obj=''):
        lower_obj = str(obj).lower()
        return super().__new__(LowerString, lower_obj)
    
    
        
# INPUT DATA:

# TEST_1:
s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))
print()
# TEST_2:
print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
print()
# TEST_3:
s = LowerString('BeeGeek')

print(s[0], s[3])
print()
# TEST_4:
words = ['NEXT', 'SITE', 'BREAK', 'CONDITION', 'SONG', 'FEDERAL', 'CHANCE', 'LEARN', 'LARGE', 'GOAL', 'GENERAL',
         'WORKER', 'BASE', 'GROWTH', 'CARRY', 'REMEMBER', 'MODEL', 'CURRENT', 'SCIENCE', 'TEACH', 'WORD', 'WEST',
         'YEAH', 'WHERE', 'NONE', 'RELATE', 'BAR', 'AUTHOR', 'GIVE', 'SKIN', 'THOUGH', 'DECIDE', 'BOOK', 'GET', 'CLOSE',
         'ARTICLE', 'QUICKLY', 'POSITIVE', 'BODY', 'CONTROL', 'PRICE', 'CONTROL', 'SIGN', 'BED', 'CITY', 'LEAVE',
         'DECISION', 'BEAT', 'WITHIN', 'TAKE', 'MISSION', 'PRESSURE', 'IF', 'TAX', 'DREAM', 'DISCOVER', 'MAJORITY',
         'MORE', 'SKILL', 'DOG', 'NEW', 'FISH', 'EDGE', 'RECOGNIZE', 'CHILD', 'ACCORDING', 'PRACTICE', 'FINANCIAL',
         'AFTER', 'FORGET', 'SHARE', 'CONCERN', 'TRIAL', 'CONDITION', 'US', 'DEFENSE', 'SECTION', 'INSTITUTION',
         'WORKER', 'THAN', 'WRITE', 'BECAUSE', 'NATIONAL', 'MANAGER', 'CULTURAL', 'THUS', 'PERSONAL', 'SEASON', 'CAR',
         'DAY', 'EAT', 'SPEECH', 'COLLEGE', 'SMALL', 'TURN', 'CUSTOMER', 'SIMILAR', 'PUBLIC', 'OFFICER', 'FISH']

for word in words:
    print(LowerString(word))

print()
# TEST_5:
print(LowerString())
print()
# TEST_6:
lowerstring = LowerString()
print(type(lowerstring))