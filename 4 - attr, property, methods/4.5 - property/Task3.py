# Реализуйте класс Person , описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# • name — имя человека
# • surname — фамилия человека

# Класс Person должен иметь одно свойство:
# • fullname — свойство, доступное для чтения и записи, возвращающее
# полное имя человека в виде строки: <имя> <фамилия>

# Примечание 1 При изменении имени и/или фамилии человека должно
# изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.

class Person:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def get_fullname(self):
        return self.name + ' ' +  self.surname
    
    def set_fullanme(self, new_full_name):
        self.name, self.surname = new_full_name.split()
        return new_full_name
        
    fullname = property(fget = get_fullname, fset = set_fullanme)    
    
# TEST_1:
person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)
print()
# TEST_2:
person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
print()
# TEST_3:
person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)
print()
# TEST_4:
person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)
print()
# TEST_5:
person = Person('Брайан', 'Керниган')
print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))    