

# НАДО ДОДЕЛАТЬ, ВРОДЕ ВСЕ ПРОСТО

# a - записать через множества



def limiter(limit, unique, lookup):
    
    def singleton(cls):
        
        a = []
        
        def get_instance(*args, **kwargs):   
            
            if (len(a) < limit):
                
                print(a)
                if a != []:
                    for classes in a:
                        for key, value in classes.items():
                            if args[0] != value[0]:
                                a.append({cls : args})
                else: a.append({cls : args})                
            
            else: 
                
                if lookup == 'FIRST': return 1
                if lookup == 'LAST': 
                    return (a[0].values())
                
            return a
        
        return get_instance
    
    return singleton


@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
obj1 = MyClass(1, 5) # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8) # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10) # создается экземпляр класса с идентификатором 3
obj4 = MyClass(4, 0) # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(2, 20) # возвращается obj2, так как экземпляр с идентификатором 2 уже есть
print(obj4.value)
print(obj5.value)