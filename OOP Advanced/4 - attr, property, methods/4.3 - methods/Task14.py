

class Wordplay:
    
    def __init__(self, words = []):
        #Чтобы экземпляр класса не зависел от изменяемого значения words
        self.words = []   
        self.words.extend(words)
        
        self.words_len = []
        self.words_only = []
        self.words_avoid = []
        
    def add_word(self, word):
        if word not in self.words: self.words.append(word)
        
    def words_with_length(self, n):
        for word in self.words:
            if len(word) == n:
                self.words_len.append(word)       
        return self.words_len
   
    def only(self, *args):
        for word in self.words:
            count = 0
            for i in range(0, len(word)):
                if word[i] in ''.join(args):
                    count += 1
            if count == len(word): self.words_only.append(word)   
        return self.words_only
    
    def avoid(self, *args):
        for word in self.words:
            count = 0
            for i in range(0, len(word)):
                if word[i] in ''.join(args):
                    count += 1
            if count == 0: self.words_avoid.append(word)   
        return self.words_avoid        


# INPUT DATA:

# TEST_1:
wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))
print()
# TEST_2:
wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)
print()
# TEST_3:
wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))
print()
# TEST_4:
wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))
print()
# TEST_5:
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))
print()
# TEST_6:
wordplay = Wordplay()
print(wordplay.words)
print()
# TEST_7:
wordplay = Wordplay(['Тьюринг', 'Торвальдс', 'Россум', 'Гейтс', 'Гамильтон', 'Бэкус', 'Кнут'])

print(wordplay.words_with_length(6))
print(wordplay.avoid('ь'))
print()
# TEST_8:
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)
print()
# TEST_9:
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)                         