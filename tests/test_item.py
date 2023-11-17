"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item_1 = Item('пылесос', 10000, 20)


def test_init():
    # Тест Создание экземпляра класса
    assert item_1.name == 'пылесос'
    assert item_1.price == 10000
    assert item_1.quantity == 20
    assert isinstance(item_1, object)


def test_all():
    #  Тест Функциональность добавление экземпляра в список созданных объектов класса
    assert len(Item.all) == 1
    item_2 = Item('телефон', 20000, 5)
    assert len(Item.all) == 2


def test_calculate_total_price():
    #  Тест Общая стоимость конкретного товара
    assert item_1.calculate_total_price() == 200000


def test_apply_discount():
    #  Тест Применение коэффициента
    Item.pay_rate = 2
    item_1.apply_discount()
    assert item_1.price == 20000
