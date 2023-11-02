# from src.item import Item
#
# if __name__ == '__main__':
#     item = Item('Телефон', 10000, 5)
#
#     # длина наименования товара меньше 10 символов
#     item.__name = 'Смартфон'
#     assert item.__name == 'Смартфон'
#
#     # длина наименования товара больше 10 символов
#     item.__name = 'СуперСмартфон'
#     # Exception: Длина наименования товара превышает 10 символов.
#
#     item_data = Item.instantiate_from_csv('/home/OlyaEf/SkyproProjects/electronics-shop-project/src/items.csv')  # создание объектов из данных файла
#     print(item_data)
#     item_all = Item.all
#     print(item_all)
#     print(len(item_all))
#     assert len(item_all) == 6  # в файле 5 таблица + 1 запись 'Телефон'
#     item1 = Item.all[0]
#     print(item1.__name)
#     # assert item1.__name == 'Телефон'  # метод переопределен
#     #
#     # assert Item.string_to_number('5') == 5
#     # assert Item.string_to_number('5.0') == 5
#     # assert Item.string_to_number('5.5') == 5


from exceptions import TooLongName
from src.item import Item


def try_long_name():
    try:
        # длина наименования товара больше 10 символов
        item.name = 'СуперСмартфон'
    except TooLongName:
        return
    # Exception: Длина наименования товара превышает 10 символов.


if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    try_long_name()

    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    print(Item.string_to_number('5.5'))
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
