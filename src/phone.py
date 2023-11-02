from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):

        """
        Инициализирует объект класса Phone.

        Args:
            name: Наименование товара.
            price: Цена товара.
            quantity: Количество товара.
            number_of_sim: Количество физических SIM-карт.

        Raises:
             ValueError: Если количество физических SIM-карт меньше или равно нулю.
        """
        super().__init__(name, price, quantity)

        if int(number_of_sim) >= 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Phone в классе отладки.
        :return: Строковое представление объекта Phone.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


