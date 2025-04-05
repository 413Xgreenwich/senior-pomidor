import pytest
from oop_lesson import BankAccount


def test_balance_after_deposit():
    account = BankAccount("Александр")
    account.deposit(100)
    balance = account.get_balance()
    assert balance > 0