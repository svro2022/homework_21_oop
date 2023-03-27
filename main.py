from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import RequestError, LogisticError


store = Store(
    items={
        "печенька": 6,
        "собачка": 2,
        "коробка": 5,
    },
)

shop = Shop(
    items={
        "собачка": 2,
        "коробка": 5,
    },
)

# общий словарь для наших словарей
storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день\n')

    while True:
        # Вывести все содержимое склада
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')


        # Запросить ввод от пользователя
        user_input = input(
            'Введите запрос в формате "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        # Распарсить и провалидировать ввод пользователя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        # запустить доставку
        # request.departure - точка отправления из общего словаря storages
        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'курьер забрал {request.amount} {request.product} из {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
        except LogisticError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f'Курьер вернул {request.amount} {request.product} в {request.departure}')
            continue





if __name__ == '__main__':
    main()


