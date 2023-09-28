
class UnitedKingdom():
    
    def capital(self):
        return 'London is the capital of great Britain'

    def language(self):
        return ('English the primary language of Great Britain')


class Spain():
    
    def capital(self):
        return ('Madrid is the capital of Spain')

    def language(self):
        return ('Spanish the primary language of Spain')
        
c1 = UnitedKingdom()       
c2 = Spain()

for country in (c1, c2):
    print(country.capital(), 'and', country.language())