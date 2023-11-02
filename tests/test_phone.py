import pytest

from src.phone import Phone


def test_repr(phone1: Phone) -> None:
    """
    Проверяет корректность вывода строкового представления объекта класса Item в классе отладки.
    """
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_init(phone1: Phone) -> None:
    """
     Проверяет инициализацию объекта класса Phone.

     Исключения:
         AssertionError: Если одно из утверждений не выполняется.
         ValueError: Если количество физических SIM-карт меньше или равно нулю.
     """
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 0
    assert phone1.number_of_sim >= 0

    with pytest.raises(ValueError) as exc_info:
        Phone('Samsung Galaxy', 90000, 3, -1)
    assert str(exc_info.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
