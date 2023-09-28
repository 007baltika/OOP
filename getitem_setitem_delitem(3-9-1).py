#Дом, в котором изначально пустые этажи, но мы можем добавлять/изменять арендатора помещения

class Building():
    
    def __init__(self, floors):
        self.floors = ['тут никто не живет'] * floors
        
        
    def __getitem__(self, company_id):
        if 0 < company_id < len(self.floors):
            return self.floors[company_id]
    
    def __setitem__(self, key, value):
        if 0 < key < len(self.floors):
            self.floors[key] = value
            
    def __delitem__(self, delete_id):
        if 0 < delete_id < len(self.floors):
            self.floors[delete_id] = 'Компания переехала в другое здание'
            
iron_building = Building(22)
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp'
iron_building[2] = 'Stark'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])                  