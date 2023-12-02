"""Тесты с использованием pytest для модуля phone."""
import pytest
from src.phone import Phone


def test_init(phone_test):
    # Тест Создание экземпляра класса
    assert phone_test.name == 'Test'
    assert phone_test.price == 10000
    assert phone_test.quantity == 10
    assert phone_test.number_of_sim == 2
    assert isinstance(phone_test, object)


def test_all():
    Phone.all.clear()
    #  Тест Функциональность добавление экземпляра в список созданных объектов класса
    item_1 = Phone("патефон", 100000, 1, 0)
    item_2 = Phone('телефон', 20000, 5, 2)
    assert len(Phone.all) == 2


def test_calculate_total_price(phone_test):
    #  Тест Общая стоимость конкретного товара
    assert phone_test.calculate_total_price() == 100000


def test_apply_discount(phone_test):
    #  Тест Применение коэффициента
    Phone.pay_rate = 2
    phone_test.apply_discount()
    assert phone_test.price == 20000


def test_instantiate_from_csv(instantiate_from_csv_test):
    assert len(Phone.all) == 5
    assert Phone.all[1].name == 'Ноутбук'


def test_string_to_number():
    assert Phone.string_to_number('5') == 5
    assert Phone.string_to_number('5.0') == 5
    assert Phone.string_to_number('5.5') == 5


def test_name_setter(phone_test):
    phone_test.name = "12345678900000000"
    assert phone_test.name == '1234567890'


def test_repr(phone_test):
    assert repr(phone_test) == "Phone('Test', 10000, 10, 2)"


def test_str(phone_test):
    assert str(phone_test) == 'Test'


def test_add(item_test, phone_test, any_test):
    assert item_test + phone_test == 20
    assert phone_test + item_test == 20
    with pytest.raises(Exception, match='Возможно сложить только с экземплярами `Phone` или `Item` классов'):
        var = phone_test + any_test


def test_number_of_sim(phone_test):
    phone_test.number_of_sim = 4
    assert phone_test.number_of_sim == 4
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone_test.number_of_sim = 0
