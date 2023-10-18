

class Wallet:
    
    def __init__(self, currency, balance):
        if isinstance(currency, str):
            if (len(currency) == 3):
                if currency[:] == currency[:].upper():
                    self.currency = currency
                else: raise ValueError("Название должно состоять только из заклавных букв")    
            else: raise NameError("Неверная длина названия валюты")    
        else: raise TypeError("Неверный тип валюты")    
        self.balance = balance
        
    def __eq__(self, another_wallet):
        
        if isinstance(another_wallet, Wallet):
            if self.currency == another_wallet.currency:
                return self.balance == another_wallet.balance
            else: raise ValueError("Нельзя сравнить разные валюты")    
        else: raise TypeError(f'Wallet не поддерживает сравнение с {another_wallet}')
        
    def __add__(self, another_wallet):
        
        if isinstance(another_wallet, Wallet):
            if self.currency == another_wallet.currency:
                return Wallet(self.currency, self.balance + another_wallet.balance)
            else: raise ValueError("Данная операция запрещена")    
        else: raise ValueError('Данная операция запрещена')
    
    def __sub__(self, another_wallet):
        
        if isinstance(another_wallet, Wallet):
            if self.currency == another_wallet.currency:
                return Wallet(self.currency, self.balance - another_wallet.balance)
            else: raise ValueError("Данная операция запрещена")    
        else: raise ValueError('Данная операция запрещена')    

#Данные для проверки
wallet1 = Wallet('USD', 50)        
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)

# wallet4 = Wallet(12, 150) <------------ отработало
# wallet5 = Wallet('qwerty', 150) <------------ отработало
# wallet6 = Wallet('abc', 150)  <------------ отработало

# print(wallet2 == wallet3) <------------ отработало
# print(wallet2 == 100) <------------ отработало
# print(wallet2 == wallet1) <------------ отработало

# wallet7 = wallet2 + wallet3 <------------ отработало
# print(wallet7.currency, wallet7.balance) <------------ отработало
# wallet2+45 <------------ отработало







