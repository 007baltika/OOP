

class BankAccount:
    
    def __init__(self, balance = 0):
        self._balance = balance
        
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else: raise ValueError('На счете недостаточно средств')    
        return self._balance
    
    def transfer(self, example_account, amount):
        if isinstance(example_account, BankAccount):
            if self._balance - amount >= 0:
                self._balance -= amount
                example_account._balance += amount
            else: raise ValueError('На счете недостаточно средств')    
            
# INPUT DATA:

# TEST_1:
account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
print()
# TEST_2:
account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)
print()
# TEST_3:
account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())
print()
# TEST_4:
account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
print()
# TEST_5:
account1 = BankAccount(balance=100)
account2 = BankAccount(balance=0)
account1.transfer(account2, 20)
print(account1.get_balance())
print(account2.get_balance())
print()
# TEST_6:
account = BankAccount()
print(hasattr(account, '_balance'))
print()
# TEST_7:
account = BankAccount(balance=10)
account.withdraw(10)
print(account.get_balance())
print()
# TEST_8:
account1 = BankAccount(balance=100)
account2 = BankAccount()
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())            
            