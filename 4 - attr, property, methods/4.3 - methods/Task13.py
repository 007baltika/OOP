

class Postman:
    
    def __init__(self):
        self.delivery_data = []
        self.houses = []
        self.apts = []
        
    def add_delivery(self, street, house, apt):
        self.delivery_data.append(tuple([street, house, apt]))
        
    def get_houses_for_street(self, street):
        filtered_streets =  filter(lambda address: address[0] == street, self.delivery_data)  
        self.houses = map(lambda house: house[1], filtered_streets)
        return list(set(self.houses))
    
    def get_flats_for_house(self, street, house):
        filtered_apts =  filter(lambda address: address[0] == street and address[1] == house, self.delivery_data)  
        self.apts = map(lambda house: house[2], filtered_apts)
        return list(set(self.apts))
    
    
# INPUT DATA:

# TEST_1:
postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))
print()
# TEST_2:
postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
print()
# TEST_3:
postman = Postman()

delivery_data = [('Тульская', 149, 35), ('Запорожская', 19, 26), ('Сосновая', 33, 17), ('Высотная', 91, 44),
                 ('Шишкина', 143, 8), ('Иванова', 60, 38), ('Веселая', 115, 19), ('Учительская', 37, 70),
                 ('М.Горького', 167, 57), ('Северная', 128, 44), ('Железнодорожная', 121, 28), ('Пригородная', 39, 2),
                 ('Одесская', 176, 34), ('Высоцкого', 100, 24), ('Цветочная', 168, 49), ('Павлова', 35, 62),
                 ('Шолохова', 177, 8), ('Баумана', 27, 96), ('Димитрова', 170, 37), ('Папанина', 85, 59),
                 ('40 лет Победы', 167, 56), ('Весенняя', 165, 63), ('Дарвина', 77, 39), ('Лунная', 200, 79),
                 ('Иванова', 104, 20), ('Комсомольская', 38, 74), ('Дарвина', 149, 44), ('Льва Толстого', 174, 85),
                 ('Победы', 64, 45), ('Новоселов', 128, 22)]

for delivery in delivery_data:
    postman.add_delivery(*delivery)

print(postman.get_houses_for_street('Дарвина'))
print(postman.get_flats_for_house('Новоселов', 128))    