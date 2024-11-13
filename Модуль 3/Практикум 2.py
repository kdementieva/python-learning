class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (float, int)) or amount < 0:
            raise ValueError('Баланс не может быть отрицательный')
        self._balance = amount 

        
    def deposit(self, amount):
        if not isinstance(amount, (float, int)) or amount <= 0:
            raise ValueError('Сумма для депозита должна быть положительной.')
        self._balance += amount 
        return self._balance
    
    def withdraw(self, amount):
        if not isinstance(amount, (float, int)) or amount > self._balance:
            raise ValueError('Недостаточно средств на счете.')
        if amount <= 0:
            raise ValueError('Сумма для снятия должна быть положительной.')
        self._balance -= amount
        return self._balance
    
    def calculate_interest(self, rate):
        if not isinstance(rate, (float, int)) or rate <= 0:
            raise ValueError('Процент должен быть положительный.')
        amount = self._balance * rate / 100
        self._balance += amount
        return self._balance

    

account1 = BankAccount(123456789, 1000)
print(account1.balance)
account1.deposit(100)
print(account1.balance)
account1.withdraw(200)
print(account1.balance)
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
account1.calculate_interest(5)
print(account1.balance)
    
