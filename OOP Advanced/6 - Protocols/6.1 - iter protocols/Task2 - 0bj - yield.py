

class DevelopmentTeam:
    
    def __init__(self):
        self.jun_names = ()
        self.sen_names = ()
    
    def add_junior(self, *jargs):
        self.jun_names += jargs    
        
    def add_senior(self, *sargs):
        self.sen_names += sargs
        
    def __iter__(self):
        yield from  iter(tuple(map(lambda jun: (jun, 'junior'), self.jun_names)))
        yield from  iter(tuple(map(lambda sen: (sen, 'senior'), self.sen_names)))
        
# TEST_1:
beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')
print()
# TEST_2:
beegeek = DevelopmentTeam()

print(len(list(beegeek)))
print()
# TEST_3:
beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')
print()
# TEST_4:
beegeek = DevelopmentTeam()

beegeek.add_senior('Arthur', 'Valery', 'Timur')
print(*beegeek, sep='\n')
print()
# TEST_5:
smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))
print()
# TEST_6:
pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))             