import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


class AnyClass:
    def __init__(self, quantity):
        self.quantity = quantity


@pytest.fixture
def any_test():
    return AnyClass(100)


@pytest.fixture
def item_test():
    return Item('Test', 10000, 10)


@pytest.fixture
def phone_test():
    return Phone('Test', 10000, 10, 2)


@pytest.fixture
def keyboard_test():
    return Keyboard('Logitech G910', 2000, 50)


@pytest.fixture
def instantiate_from_csv_test():
    Item.all.clear()
    Item.instantiate_from_csv('items.csv')
    return Item.all
