import json
from uuid import uuid4


def load_dict() -> list:
    """
    Ф-я загружає список словників в json-файлу
    :param:
    :return: products -- список словників з переліком продуктів, їх категорій та ціною
    """
    file = "catalog_products.json"
    products = json.load(open(file, mode='r'))
    return products


def view_index(index_sep: dict, d: dict):
    """
    Ф-ія виводить в спеціально підготовленому вигляді продукти та ціни на них,
        згрупованні по index_sep
    :param index_sep: індекс, словник списком.
        key - унікальні назви продуктів в індексі
        value - списки унікальних uid продуктів та ціни на них
    :param d: дані продувктів промарковані уникальним uid
    :return: -
    """
    i = 0
    for key, values in index_sep.items():
        i += 1
        print(f'{i}. {key.capitalize()}:')
        for uid in values:
            print(f'   {d[uid]["name"]} -- price {d[uid]["price"]} UAH')


catalog = load_dict()
# індекс продуктів, унікальне значення
uid_index = dict()
category_index = dict()
for product in catalog:
    product['uid'] = str(uuid4())
    uid_index[product['uid']] = product
    if product['category'] in category_index:
        category_index[product['category']].append(product['uid'])
    else:
        category_index[product['category']] = list()
        category_index[product['category']].append(product['uid'])

print('\nProducts by Category\n')
view_index(category_index, uid_index)
