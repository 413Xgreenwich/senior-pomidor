class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print() # todo: add info output f-string about deposit
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print() # todo add info
        else:
            print() # todo add info about error
    def get_balance(self):
        print(self.__balance)


class SavingsAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass

