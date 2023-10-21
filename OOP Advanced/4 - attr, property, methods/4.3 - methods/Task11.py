

class TextHandler:
    
    def __init__(self):
        self.words = []
        
    def add_words(self, word):
        self.words += word.split()
        print(self.words)
        
    def get_shortest_words(self):
        if self.words != []:
            len_min = min(map(lambda word: len(word), self.words))
        return list(filter(lambda word: len(word) == len_min, self.words))
    
    def get_longest_words(self):
        if self.words != []:
            len_max = max(map(lambda word: len(word), self.words))
        return list(filter(lambda word: len(word) == len_max, self.words))
    

# INPUT DATA:

# TEST_1:
texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
print()
# TEST_2:
texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
print()
# TEST_3:
texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky, never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
print()
# TEST_4:
texthandler = TextHandler()
texthandler.add_words('''Я помню чудное мгновенье
Передо мной явилась ты
Как мимолетное виденье
Как гений чистой красоты

В томленьях грусти безнадежной
В тревогах шумной суеты
Звучал мне долго голос нежный
И снились милые черты

Шли годы Бурь порыв мятежный
Рассеял прежние мечты
И я забыл твой голос нежный
Твои небесные черты

В глуши во мраке заточенья
Тянулись тихо дни мои
Без божества без вдохновенья
Без слез без жизни без любви

Душе настало пробужденье
И вот опять явилась ты
Как мимолетное виденье
Как гений чистой красоты

И сердце бьется в упоенье
И для него воскресли вновь
И божество и вдохновенье
И жизнь и слезы и любовь''')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())            