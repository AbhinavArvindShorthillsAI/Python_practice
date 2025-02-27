
import pytest
from unit_testing import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -1

def test_multiply(calculator):
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-2, 3) == -6

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3

    with pytest.raises(ValueError):
        calculator.divide(5, 0)
