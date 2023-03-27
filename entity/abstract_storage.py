from abc import ABC, abstractmethod


# name-название, amount-количество
# AbstractStorage(ABC) - абстрактный класс (методы-шаблоны для других классов (поэтому методы пустые))


class AbstractStorage(ABC):

    # добавление предмета на склад
    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    # удаление предмета со склада
    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    # расчет свободного места на складе
    @abstractmethod
    def get_free_space(self) -> int:
        pass

    # получение всех предметов на складе
    @abstractmethod
    def get_items(self):
        pass

    # возвращает количество уникальных товаров
    @abstractmethod
    def get_unique_items_count(self):
        pass
