"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price(item1, item2):
    """Проверка расчета цены."""
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(item1, item2):
    item1.pay_rate = 0.9  # устанавливаем скидку 10%
    item1.apply_discount()
    assert item1.price == 9000.0
    item2.pay_rate = 0.85  # устанавливаем скидку 15%
    item2.apply_discount()
    assert item2.price == 17000.0


def test_pay_rate(item1, item2):
    assert item1.pay_rate == 1.0
    assert item2.pay_rate == 1.0


def test_all_items(item1, item2, all_items):
    assert len(all_items) == 2
    assert item1 in all_items
    assert item2 in all_items
