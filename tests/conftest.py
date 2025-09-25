import pytest
from src import *

@pytest.fixture()
def calc():
    return Calc()

@pytest.fixture()
def user():
    def make_user(name=None, email=None, age=None):
        return User(name, email, age)
    return make_user