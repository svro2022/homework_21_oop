from entity.base_storage import BaseStorage
from exceptions import TooManyDifferentProducts

# Максимальная вместимость capacity по умолчанию 20


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        # Проверить, есть ли такой товар и
        # в магазине не больше 5 разных товаров
        # если товара нет в словаре (нет такого ключа) и количество разных товаров >= 5, ошибка
        if name not in self.get_items() and self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(name, amount)
