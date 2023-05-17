from typing import List

import pytest

from exceptions import TooLongName
from src.item import Item
from src.phone import Phone


def test_calculate_total_price(item1: Item, item2: Item, all_items: List[Item]) -> None:
    """
    Проверяет, что метод calculate_total_price() корректно рассчитывает
    общую цену для товаров.
    """
    assert all_items == [item1, item2]
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(item1: Item, item2: Item) -> None:
    """
    Проверяет, что метод apply_discount() корректно устанавливает
    скидку на товар и изменяет его цену.
    """
    item1.pay_rate = 0.9  # устанавливаем скидку 10%
    item1.apply_discount()
    assert item1.price == 9000.0
    item2.pay_rate = 0.85  # устанавливаем скидку 15%
    item2.apply_discount()
    assert item2.price == 17000.0


def test_pay_rate(item1: Item, item2: Item) -> None:
    """
    Проверяет, что начальное значение pay_rate устанавливается
    правильно для всех товаров.
    """
    assert item1.pay_rate == 1.0
    assert item2.pay_rate == 1.0


def test_all_items(item1: Item, item2: Item, all_items: List[Item]) -> None:
    """
    Проверяет, что список all_items содержит все товары и только их.
    """
    assert len(all_items) == 2
    assert item1 in all_items
    assert item2 in all_items


def test_name(item1: Item) -> None:
    """
    Проверяет, что name.setter корректно обрабатывает длину строки при установке имени товара.
    """
    # Установка корректного значения имени
    item1.name = "Ноутбук"
    assert item1.name == "Ноутбук"
    with pytest.raises(TooLongName):
        item1.name = 'Это наименование товара более 10 символов'


def test_instantiate_from_csv(tmp_path: str) -> None:
    """
    Проверяет, что метод instantiate_from_csv() корректно считывает данные
    из файла CSV и создает объекты Item.
    """
    data = Item.instantiate_from_csv('/home/OlyaEf/SkyproProjects/electronics-shop-project/src/items.csv')
    assert len(data) == 5
    assert data[0].name == 'Смартфон'
    assert data[0].price == 100
    assert data[0].quantity == 1
    assert data[1].name == 'Ноутбук'
    assert data[2].price == 10
    assert data[3].quantity == 5
    assert data[4].name == 'Клавиатура'


def test_string_to_number() -> None:
    """
    Проверяет, что метод string_to_number() корректно преобразует строку в число.
    """
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('5.75') == 5.0
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('-2') == -2


def test_repr(item1: Item) -> None:
    """
    Проверяет корректность вывода строкового представления объекта класса Item в классе отладки.
    """
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1: Item) -> None:
    """
    Проверяет корректность вывода строкового представления объекта класса Item для пользовательского представления.
    """
    assert str(item1) == 'Смартфон'


def test_add(item1, item2, phone1, phone2):
    """
    Проверяет операцию сложения (`+`) для объектов типов Item и Phone.

    Исключения:
            AssertionError: Если одно из утверждений не выполняется.
        """
    assert item1 + item2 == 25
    assert phone1 + phone2 == 7
    assert item1 + phone1 == 25
    assert item2 + phone2 == 7

    phone = Phone('iPhone 14', 120000, 5, 2)
    other = 'Not an Item or Phone object'
    with pytest.raises(TypeError):
        assert phone + other == TypeError
