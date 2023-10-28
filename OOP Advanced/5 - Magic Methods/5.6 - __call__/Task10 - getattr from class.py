

class SortKey:
    
    def __init__(self, *args):
        self.atributs_for_sort = args
        
    def __call__(self, instance):
        print(instance)
        return [getattr(instance, attribute) for attribute in self.atributs_for_sort]

    
     
     
class User:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'User({self.name}, {self.age})'
    
    
    
    
users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))        #[User(Arthur, 20), User(Gvido, 67), User(Gvido, 60), User(Timur, 30), User(Timur, 45)]
print(sorted(users, key=SortKey('name', 'age'))) #[User(Arthur, 20), User(Gvido, 60), User(Gvido, 67), User(Timur, 30), User(Timur, 45)]
print(sorted(users, key=SortKey('age')))         #[User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)] 
print(sorted(users, key=SortKey('age', 'name'))) #[User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]       