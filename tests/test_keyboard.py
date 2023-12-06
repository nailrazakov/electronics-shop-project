"""Тесты с использованием pytest для модуля keyboard."""
import pytest
from src.keyboard import Keyboard


def test_init(keyboard_test):
    # Тест Создание экземпляра класса
    assert keyboard_test.name == 'Logitech G910'
    assert keyboard_test.price == 2000
    assert keyboard_test.quantity == 50
    assert keyboard_test.language == 'EN'
    assert isinstance(keyboard_test, object)


def test_change_lang(keyboard_test):
    # Изменить язык можно только методом `change_lang()`
    assert keyboard_test.language == 'EN'
    keyboard_test.change_lang()
    assert keyboard_test.language == 'RU'
    keyboard_test.change_lang()
    assert keyboard_test.language == 'EN'


def test_all():
    #  Тест Функциональность добавление экземпляра в список созданных объектов класса
    Keyboard.all.clear()
    keyboard_1 = Keyboard("Электроника", 500, 100)
    keyboard_2 = Keyboard('Волна-4', 350, 50)
    assert len(Keyboard.all) == 2


def test_calculate_total_price(keyboard_test):
    #  Тест Общая стоимость конкретного товара
    assert keyboard_test.calculate_total_price() == 100000


def test_apply_discount(keyboard_test):
    #  Тест Применение коэффициента
    Keyboard.pay_rate = 2
    keyboard_test.apply_discount()
    assert keyboard_test.price == 4000


def test_string_to_number():
    assert Keyboard.string_to_number('5') == 5
    assert Keyboard.string_to_number('5.0') == 5
    assert Keyboard.string_to_number('5.5') == 5


def test_name_setter(keyboard_test):
    keyboard_test.name = "12345678900000000"
    assert keyboard_test.name == '1234567890'


def test_repr(keyboard_test):
    assert repr(keyboard_test) == "Keyboard('Logitech G910', 2000, 50)"


def test_str(keyboard_test):
    assert str(keyboard_test) == 'Logitech G910'
