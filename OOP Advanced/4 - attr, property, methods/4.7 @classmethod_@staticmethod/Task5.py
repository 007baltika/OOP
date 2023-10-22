# Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен принимать никаких аргументов.

# Класс StrExtension должен иметь три статических метода:

# remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
# leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
# replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все символы из chars на char с учетом регистра 
# и возвращает полученный результат.

from string import ascii_letters

class StrExtension:
    
    @staticmethod
    def remove_vowels(stroka):
        return ''.join(filter(lambda symbol: symbol if symbol not in 'aeiouyAEIOUY' else '', stroka))
            
    @staticmethod
    def leave_alpha(stroka):
        return ''.join(filter(lambda symbol: symbol if symbol in ascii_letters else '', stroka))
    
    @staticmethod
    def replace_all(stroka, chars, char):
        new_string = map(lambda bukva: char if bukva in chars else bukva, stroka)
        return ''.join(list(new_string))
    
# INPUT DATA:

# TEST_1:
print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print()
# TEST_2:
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print()
# TEST_3:
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
print()
# TEST_4:
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'))
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'.upper()))
print()
# TEST_5:
print(StrExtension.leave_alpha('beegeek!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~BEEGEEK'))
print(StrExtension.leave_alpha('beegeek0123456789BEEGEEK'))
print()
# TEST_6:
from string import ascii_lowercase

text = '''I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.'''

print(StrExtension.remove_vowels(text))
print(StrExtension.leave_alpha(text))
print(StrExtension.replace_all(text, ascii_lowercase, ''))    