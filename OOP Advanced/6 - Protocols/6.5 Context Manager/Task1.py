# класс - контекстный менеджер, подавление любых ошибок

class SuppressAll:
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args, **keargs):
        return True
    
# TEST_1:
print('start')

with SuppressAll():
    print('Python generation!')
    raise ValueError

print('end')
print()
# TEST_2:
print('start')

with SuppressAll():
    print('Python generation!')

print('end')
print()
# TEST_3:
print('start')

with SuppressAll():
    print(2077 / 0)
    print('Python generation!')

print('end')
print()
# TEST_4:
un_ord_me = [1054, 1090, 1074, 1077, 1090, 32, 1085, 1072, 32, 1074, 1086, 1087, 1088, 1086, 1089, 32, 1087, 1086, 1095,
             1077, 1084, 1091, 32, 1042, 1072, 1083, 1077, 1088, 1072, 32, 1090, 1072, 1082, 1086, 1081, 32, 1089, 1091,
             1088, 1086, 1074, 1099, 1081, 32, 1073, 1091, 1076, 1077, 1090, 32, 1074, 32, 1089, 1083, 1077, 1076, 1091,
             1102, 1097, 1077, 1084, 32, 1091, 1088, 1086, 1082, 1077, 46, 32, 1057, 1084, 1086, 1090, 1088, 1080, 32,
             1074, 1085, 1080, 1084, 1072, 1090, 1077, 1083, 1100, 1085, 1086, 33]

with SuppressAll():
    print(un_ord_me)
    raise TypeError