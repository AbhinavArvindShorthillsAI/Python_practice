from unittest.mock import patch
import pytest
from mocks import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount(balance=500)

@patch("mocks.requests.get")
def test_validate_transaction(mock_get, bank_account):
    """Mock the API response for transaction validation."""
    # Mock API response for an approved transaction
    mock_get.return_value.json.return_value = {"status": "approved"}
    
    assert bank_account.validate_transaction("12345") is True

    # Mock API response for a failed transaction
    mock_get.return_value.json.return_value = {"status": "failed"}

    assert bank_account.validate_transaction("67890") is False
