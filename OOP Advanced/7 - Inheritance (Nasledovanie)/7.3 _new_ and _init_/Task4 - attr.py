# Реализуйте класс TitledText , наследника класса str , который описывает
# текст, имеющий заголовок. При создании экземпляра класс должен принимать
# два аргумента в следующем порядке:
    
# • content — текст
# • text_title — заголовок текста
# Класс TitleText должен иметь один метод экземпляра:
# • title() — метод, возвращающий заголовок текста

# Примечание 1 Значением экземпляра класса TitledText должен быть именно
# текст, а не заголовок текста или текст вместе с заголовком.

class TitledText(str):
    
    def __new__(cls, content, text_title):
        example = super().__new__(TitledText, content)
        TitledText.text_title = text_title
        return example
    
    def title(self):
        return TitledText.text_title
    
    
    
# INPUT DATA:

# TEST_1:
titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))
print()
# TEST_2:
titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)
print()
# TEST_3:
headlines = ['Как полностью изменить...', 'Где найти …', 'Быстрый способ...', 'Ошибки, которые приведут тебя к ...',
             'Как быстро...']
contents = ['Нужно всего лишь...', 'Обратитесь к нам, и мы всё расскажем', 'Для этого Вы должны', 'Не делай их',
            'Ну это вообще просто']

for heading, content in zip(headlines, contents):
    titledtext = TitledText(content, heading)
    print(titledtext.title(), titledtext)