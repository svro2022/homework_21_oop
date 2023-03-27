from entity.base_storage import BaseStorage

# В нем хранится любое количество любых товаров.
# Максимальная вместимость capacity по умолчанию 100
# super() - обращение к классу-родителю и передача ему items, capacity


class Store(BaseStorage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)
