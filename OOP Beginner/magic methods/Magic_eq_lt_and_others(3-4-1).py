#Задача на сравнение чисел со значениями экземпляров и сравнение двух экземпляров

class ChessPlayer():
    
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating
    
    def __eq__(self, nums_or_classexample):
        
        if isinstance(nums_or_classexample, int):
            return self.rating == nums_or_classexample
        
        if isinstance(nums_or_classexample, ChessPlayer):
            return self.rating == nums_or_classexample.rating
        
        if not isinstance(nums_or_classexample, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        
    def __gt__(self, nums_or_classexample):
        
        if isinstance(nums_or_classexample, int):
            return self.rating > nums_or_classexample
        
        if isinstance(nums_or_classexample, ChessPlayer):
            return self.rating > nums_or_classexample.rating
        
        if not isinstance(nums_or_classexample, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        
    def __lt__(self, nums_or_classexample):
        
        if isinstance(nums_or_classexample, int):
            return self.rating < nums_or_classexample
        
        if isinstance(nums_or_classexample, ChessPlayer):
            return self.rating < nums_or_classexample.rating
        
        if not isinstance(nums_or_classexample, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        
Console.ReadLine()                  