import pytest

from src.keyboard import KeyBoard


def test_init(kb: KeyBoard) -> None:
    """
    Проверяет инициализацию объекта KeyBoard.
    """
    assert str(kb) == "Dark Project KD87A"


def test_change_lang_with_valid_lang(kb: KeyBoard) -> None:
    """
    Проверяет изменение языка на допустимый язык.
    """
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_change_lang_with_invalid_lang(kb: KeyBoard) -> None:
    """
    Проверяет изменение языка на недопустимый язык.
    """
    with pytest.raises(AttributeError) as exc_info:
        kb.change_lang('CH')
    assert str(exc_info.value) == 'AttributeError'


def test_change_lang_with_default_lang(kb: KeyBoard) -> None:
    """
    Проверяет изменение языка на язык по умолчанию.
    """
    kb.change_lang()
    assert kb.language == 'RU'

