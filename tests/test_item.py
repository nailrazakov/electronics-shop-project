"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_init(item_test):
    # Тест Создание экземпляра класса
    assert item_test.name == 'Test'
    assert item_test.price == 10000
    assert item_test.quantity == 10
    assert isinstance(item_test, object)


def test_all():
    #  Тест Функциональность добавление экземпляра в список созданных объектов класса
    item_1 = Item("патефон", 100000, 1)
    item_2 = Item('телефон', 20000, 5)
    assert len(Item.all) == 3


def test_calculate_total_price(item_test):
    #  Тест Общая стоимость конкретного товара
    assert item_test.calculate_total_price() == 100000


def test_apply_discount(item_test):
    #  Тест Применение коэффициента
    Item.pay_rate = 2
    item_test.apply_discount()
    assert item_test.price == 20000


def test_instantiate_from_csv(instantiate_from_csv_test):
    assert len(Item.all) == 5
    assert Item.all[1].name == 'Ноутбук'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_setter(item_test):
    item_test.name = "12345678900000000"
    assert item_test.name == '1234567890'
