from collections import defaultdict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughProduct, NotEnoughSpace, UnknownProduct


# items - словарь {название предмета (name): количество предмета(amount)}
# capacity - емкость склада (сколько всего влезает туда предметов)
# можно self.__items = defaultdict(default_factory)
# defaultfactory собирает значения (если их нет, то получим [], а не KeyError)
# int - просто числа (если ключа нет, получим 0)


class BaseStorage(AbstractStorage):
    def __init__(self, items, capacity):
        # self.__items = defaultdict(int)
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        # Проверить, что места на складе достаточно (если оставшееся место на складе < количество предметов)
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        # Добавить товар
        # from collections import defaultdict
        # self.__items[name] += amount
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        # Проверить есть ли такой товар и хватает ли его на складе
        # Если товар не на складе, ошибка
        # Если количества не хватает, ошибка
        if name not in self.__items:
            raise UnknownProduct
        if self.__items[name] < amount:
            raise NotEnoughProduct

        # Вычесть необходимое количество товара.
        # Если товара станет 0, удалить товар из списка.
        self.__items[name] -= amount
        if self.__items[name] == 0:
            del self.__items[name]

    def get_free_space(self) -> int:
        # Сколько осталось места на складе.
        # Считаем сумму значений в словаре __items.
        # Вычесть ее из __capacity
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        # Получение всего словаря __items
        return self.__items

    def get_unique_items_count(self):
        # Получение уникальных товаров на складе.
        # Считаем длину словарика __items
        return len(self.__items)
        # return len(self.__items.keys()) - тоже самое
