#Собака, ее age и что она говорит 

class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        print(self.name, ' is ', self.age, ' years old')
   

    def speak(self, sound):
        print(self.name, ' says ', sound)

Console.ReadLine()   