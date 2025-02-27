import pytest
from fixtures import BankAccount

@pytest.fixture
def bank_account():
    """Fixture to create a bank account instance before each test."""
    return BankAccount(balance=100)

def test_deposit(bank_account):
    assert bank_account.deposit(50) == 150
    assert bank_account.deposit(100) == 250

def test_withdraw(bank_account):
    assert bank_account.withdraw(30) == 70
    assert bank_account.withdraw(70) == 0

    with pytest.raises(ValueError, match="Insufficient funds"):
        bank_account.withdraw(10)  # Should raise an error

def test_get_balance(bank_account):
    assert bank_account.get_balance() == 100
