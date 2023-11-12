# Реализуйте класс PremiumUser , наследника класса User , описывающий
# пользователя некоторого интернет-ресурса с премиум подпиской. Процесс
# создания экземпляра класса PremiumUser должен совпадать с процессом
# создания экземпляра класса User .

class User:
    
    def __init__(self, name):
        self.name = name
        
    def skip_ads(self):
        return False
    
class PremiumUser(User):
    def __init__(self, name):
        User.__init__(self, name)
    
    def skip_ads(self):
        return True            
    
    
# INPUT DATA:

# TEST_1:
print(issubclass(PremiumUser, User))
print()
# TEST_2:
user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())
print()
# TEST_3:
names = ['Наина', 'Татьяна', 'Наркис', 'Наталья', 'Вацлав', 'Пахом', 'Соломон', 'Григорий', 'Жанна', 'Арефий', 'Раиса',
         'Анжелика', 'Евгений', 'Валерия', 'Ия', 'Фрол', 'Милица', 'Ирина', 'Лукьян', 'Никита', 'София', 'Агафья',
         'Рубен', 'Александра', 'Алевтина', 'Нина', 'Касьян', 'Фадей', 'Прасковья', 'Оксана', 'Дементий', 'Анна',
         'Алла', 'Радислав', 'Амос', 'Анатолий', 'Венедикт', 'Аникита']

for name in names:
    user = User(name)
    premium_user = PremiumUser(name)

    print(user.skip_ads())
    print(premium_user.skip_ads()) 