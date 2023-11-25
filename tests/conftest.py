import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item('Test', 10000, 10)


@pytest.fixture
def instantiate_from_csv_test():
    Item.all.clear()
    Item.instantiate_from_csv('items.csv')
    return Item.all
