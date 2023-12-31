# Контекстный менеджер должен выводить строку tag при входе в блок with и
# после выхода из блока with .


from contextlib import contextmanager
@contextmanager

def make_tag(tag):
    print(tag)
    yield None
    print(tag)
    
# TEST_1:
with make_tag('---'):
    print('Поколение Python')
print()
# TEST_2:
with make_tag('**********'):
    print('Челябинск')
print()
# TEST_3:
with make_tag('--- Ломтик хлеба ---'):
    print('томат | салат | сыр | бекон')
print()
# TEST_4:
with make_tag('*' * 20), make_tag(' ' * 5 + '-' * 10), make_tag(' ' * 7 + '=' * 6):
    print(' ' * 7 + 'привет')