#Статистика игрока

class SoccerStat():
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
    
    def score(self, goals = 1):
        self.goals = goals
        #return goals
        
    def make_assist(self, assists = 1):
        self.assists = assists
        #return assists
    
    def statistics(self):
        print(self.name, ' ', self.surname, ' - голы: ',  self.goals, ', передачи: ', self.assists)    
        
Console.ReadLine()         