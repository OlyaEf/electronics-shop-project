from src.item import Item


class LangMixin:
    """
    Миксин-класс, предоставляющий функциональность языка.
    """
    def __init__(self):
        self.__language: str = 'EN'

    def change_lang(self) -> None:
        """
        Изменить язык на 'EN' или 'RU'.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self) -> str:
        """
        Получить текущий язык.
        """
        return self.__language

    @language.setter
    def language(self, new_lang: str) -> None:
        """
        Сеттер для свойства языка. В этой реализации игнорируется.
        """
        pass  # Игнорируем попытку установить язык


class KeyBoard(Item, LangMixin):
    """
    Класс Keyboard, наследующийся от Item и LangMixin.
    """
    def __init__(self, name: str, price: float, quality: int) -> None:
        """
        Инициализация экземпляра Keyboard.
        Args:
            name (str): Название клавиатуры.
            price (float): Цена клавиатуры.
            quality (int): Количество клавиатур.
        """
        super().__init__(name, price, quality)
        LangMixin.__init__(self)

    def change_lang(self) -> 'KeyBoard':
        """
        Изменить язык и вернуть экземпляр KeyBoard.
        Returns:
            KeyBoard: Экземпляр KeyBoard.
        """
        super().change_lang()
        return self
