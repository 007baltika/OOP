# Назовем скобочной последовательностью строку, состоящую из символов ( и ) . 
#   Будем считать скобочную последовательность правильной, если: 
# - для каждой открывающей скобки есть закрывающая скобка
# - скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее

# Напишите программу, которая определяет, является ли скобочная последовательность правильной.


def skobe(stroka):
    
    stroka = list(stroka)
    # print(stroka)
    
    if stroka.count('(') == stroka.count(')') and len(stroka) > 1:

        for i in range(0, len(stroka) - 1):
            
            if stroka[i] == '(' and i < stroka.index(')'):
                stroka[i] = True
                stroka[stroka.index(')')] = True    
        
        return len(set(stroka)) == 1 
           
    else: return False   

# Тестовые данные

# print(skobe('()()()')) 
# print(skobe('(())')) 
# print(skobe('()()()(')) 
# print(skobe(')(')) 

# print(skobe('(()))'))
# print(skobe('(()()())'))
# print(skobe('()()())'))
# print(skobe('(())))(()((()))(()())((()'))

# print(skobe('((())((())))(())()'))
# print(skobe('((()))'))
# print(skobe(')'))
# print(skobe('('))

# print(skobe(')()('))
# print(skobe('(()()(()()))'))
# print(skobe('((())((())))(())()(()()(()()))(()()(()()))((())((())))(())()((()))'))
# print(skobe('())('))

# print(skobe('())(()'))

 