import pytest as pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def all_items(item1, item2):
    return [item1, item2]


