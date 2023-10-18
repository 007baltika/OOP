
class Initialization():
    
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else: print('Количество людей должно быть целым числом')
        
class Vegetarian(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)   
        
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
    
class MeatEater(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)   
        
    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'    
    
class SweerTooth(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)   
        
    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'    
                
    def  __eq__(self, num_or_class):
        
        if isinstance(num_or_class, int):
            return num_or_class == self.capacity
        
        elif isinstance(num_or_class, (Vegetarian, MeatEater)):
            return self.capacity == num_or_class.capacity     
        
        else: return f'Невозможно сравнить количество сладкоежек с {num_or_class}'     
        
    def __lt__(self, num_or_class):
        
        if isinstance(num_or_class, int):
            return self.capacity < num_or_class
        
        elif isinstance(num_or_class, (Vegetarian, MeatEater)):
            return self.capacity < num_or_class.capacity     
        
        else: return f'Невозможно сравнить количество сладкоежек с {num_or_class}'   
        
    def __gt__(self, num_or_class):
        
        if isinstance(num_or_class, int):
            return self.capacity > num_or_class
        
        elif isinstance(num_or_class, (Vegetarian, MeatEater)):
            return self.capacity > num_or_class.capacity     
        
        else: return f'Невозможно сравнить количество сладкоежек с {num_or_class}'             
        

v_first = Vegetarian(10000, ['Орехи', 'Овощи', 'Фрукты'])
print(v_first)

v_second = Vegetarian([23], ['nothing'])

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)

s_first = SweerTooth(30000, ['Мороженое', 'Чипсы', 'Шоколад'])
print(s_first) 

print(s_first > v_first) 
print(30000 == s_first)
print(s_first == 25000)
print(100000 < s_first)
print(100 < s_first)      