import pytest
from src.calc import Calc

@pytest.fixture()
def calc():
    return Calc()