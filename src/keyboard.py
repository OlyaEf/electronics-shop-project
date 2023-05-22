from src.item import Item


class KeyBoard(Item):
    """
    Класс, представляющий клавиатуру.
    """
    language: str = 'EN'

    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализация объекта KeyBoard.
        Параметры:
            name (str): Название клавиатуры.
            price (float): Цена клавиатуры.
            quantity (int): Количество клавиатур.
        """
        super().__init__(name, price, quantity)

    def change_lang(self, new_lang: str = 'RU') -> 'KeyBoard':
        """
        Изменяет язык клавиатуры.
        Параметры:
            new_lang (str): Новый язык клавиатуры. По умолчанию - 'RU'.
        Возвращает:
            KeyBoard: Объект KeyBoard с измененным языком.
        """
        if new_lang.lower() == 'en':
            self.language = 'EN'
        elif new_lang.lower() == 'ru':
            self.language = 'RU'
        else:
            raise AttributeError('AttributeError')
        return self


class KeyboardMixin:
    """
    Миксин, представляющий функциональность изменения раскладки клавиатуры.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация объекта KeyboardMixin.
        """
        super().__init__(*args, **kwargs)
        self.keyboard_layout = 'QWERY'

    def change_layout(self, new_layout: str) -> None:
        """
        Изменяет раскладку клавиатуры.
        Параметры:
            new_layout (str): Новая раскладка клавиатуры.
        """
        self.keyboard_layout = new_layout
