import csv
from typing import List, Union
from exceptions import TooLongName


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Item в читабельном формате.
        :return: Строковое представление объекта Item.
        """
        return f"{self.name} ({self.quantity} шт.) - {self.price}р."

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Возвращает название товара.
        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название товара.
        :param name: Название товара.
        :raises TooLongName: Если название товара длиннее 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise TooLongName('Это наименование товара более 10 символов')

    @staticmethod
    def string_to_number(string: str) -> Union[int, float]:
        """
        Преобразует строку в целое число или число с плавающей запятой, в зависимости от наличия точки в строке.
        :param string: Строка, которую нужно преобразовать в число.
        :return: Целое число или число с плавающей запятой.
        """
        if '.' in string:
            return float(string) // 1
        else:
            return int(string)

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> List:
        """
        Создание экземпляров класса Item из CSV-файла.
        :param file_path: Путь к файлу CSV.
        :return: Список экземпляров класса Item.
        """
        cls.all = []
        items = []
        cls.file_path = file_path
        with open(file_path, 'r', encoding='windows-1251') as f:
            reader = csv.reader(f)
            next(reader)  # пропускает заголовки столбцов
            for row in reader:
                name = row[0]
                price = cls.string_to_number(row[1])
                quantity = cls.string_to_number(row[2])
                items.append(cls(name, price, quantity))
        return items
