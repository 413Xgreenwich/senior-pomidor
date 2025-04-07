import pytest


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"На банковский счёт {self.owner} поступила сумма в размере {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"С банковского счёта {self.owner} выведена сумма в размере {amount}")
        else:
            print(
                f"Неуспешная попытка вывести сумму со счёта {self.owner}: баланс счёта ниже требуемой суммы"
            )

    def get_balance(self):
        print(f"Баланс счёта {self.owner}: {self.__balance}")
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._BankAccount__balance += amount
            print(
                f"На сберегательный счёт {self.owner} поступила сумма в размере {amount}"
            )

    def apply_interest(self):
        added_sum = self._BankAccount__balance * self.interest_rate
        self._BankAccount__balance += added_sum
        print(
            f"На счёт {self.owner} начислены проценты на остаток в размере {added_sum}. Сумма на счёте - {self._BankAccount__balance}"
        )


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def deposit(self, amount):
        if amount > 0:
            self._BankAccount__balance += amount
            print(f"На рассчётный счёт {self.owner} поступила сумма в размере {amount}")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"С банковского счёта {self.owner} выведена сумма в размере {amount}")


account1 = SavingsAccount("Александр")
print(account1.owner)
account1.get_balance()
account1.deposit(500)
account1.withdraw(100)
account1.apply_interest()
account1.get_balance()

