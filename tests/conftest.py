import pytest as pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def phone1():
    return Phone('iPhone 14', 120000, 5, 2)


@pytest.fixture
def phone2():
    return Phone('Phone 5', 800.0, 2, 1)


@pytest.fixture
def all_items(item1, item2):
    return [item1, item2]


