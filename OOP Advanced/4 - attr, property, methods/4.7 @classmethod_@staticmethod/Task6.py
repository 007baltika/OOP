
#Надо доделать to_upper_camel, остальное все работает

from string import ascii_letters
class CaseHelper:
    
    @staticmethod
    def is_snake(string):
        return ('_' in string.strip('_')[1:-1] and string.islower()) or string.islower()
    
    @staticmethod
    def is_upper_camel(string):
        return '_' not in string and string[0].isupper()
    
    @staticmethod
    def to_snake(string_UCC):
        new_string = map(lambda symbol: '_' + symbol.lower() if symbol.isupper() else symbol.lower(), string_UCC[1:-1])
        return string_UCC[0].lower() + ''.join(list(new_string)) + string_UCC[-1].lower()
    
    @staticmethod
    def to_upper_camel(string_s_c):
        new_string = list(string_s_c)
        out_string = []
        for i in range(1, len(new_string) - 1):
            if out_string[i-1].isupper(): continue
            elif new_string[i] == '_': out_string.append(new_string[i + 1].upper())
            else: out_string.append(new_string[i])
        return string_s_c[0].upper() + ''.join(out_string[1:-1]) + string_s_c[-1].lower()

print(CaseHelper.to_upper_camel('bee_geek'))    

# INPUT DATA:

# TEST_1:
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
print()
# TEST_2:
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
print()
# TEST_3:
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
print()
# TEST_4:
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
print()
# TEST_5:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))
print()
# TEST_6:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))
print()
# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))
print()
# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))