import json
from Laptop import Laptop
from Headphone import Headphone
from SmartWatch import SmartWatch


def load_dict() -> list:
    """
    :return: список словників, імпортованих з json-файлу
    """
    file = "database-tech.json"
    tech = json.load(open(file, mode='r', encoding='utf-8'))
    return tech


def category_lists():
    """
    :return: повертає список категорій товарів
    """
    for row in catalog:
        if row['category'] == 'Ноутбуки':
            Laptop.category = row['category']
        elif row['category'] == 'Навушники':
            Headphone.category = row['category']
        elif row['category'] == 'Смарт-годинники':
            SmartWatch.category = row['category']
    category_list1 = [Laptop.category, Headphone.category, SmartWatch.category]
    return category_list1


def category_input(detail_list):
    """
    Користувач обирає категорію/ціну/іншу х-ку товару із запропонованого списку
    :return: обрану користувачем х-ку для фільтрування
    """
    while True:
        choice_cat = input('''Виберіть одну з характеристик.
 >>     ''')
        if choice_cat in detail_list:
            return choice_cat
            break
        else:
            print('Введіть категорію з вище перелічених')


def check_category() -> list:
    """
    :return: список словників після застосування фільтру "Категорія"
    """
    menu_1 = list()
    for row1 in catalog:
        if row1['category'] == k:
            Laptop.__init__ = row1
            menu_1.append(Laptop.__init__)
        elif row1['category'] == k:
            Headphone.__init__ = row1
            menu_1.append(Headphone.__init__)
        elif row1['category'] == k:
            SmartWatch.__init__ = row1
            menu_1.append(SmartWatch.__init__)
    return menu_1


def group_category(menu_category):
    """
    :param menu_category: список словників після застосування фільтрів
    :return: назву товару з основними характеристиками з menu_category
    """
    for r_menu in menu_category:
        print(f"{r_menu['name']}\n\
    Ціна: {r_menu['price']} UAH \n\
    В наявності: {r_menu['quantity']} од.")
        for key, value in r_menu['additional_fields'].items():
            print(f'    {key}: {value}')


def group_fltr(menu_category):
    """
    :param menu_category: список словників, який попередньо був відфільтрований
    :return: список назв фільтрів
    """
    fltr_list = ["Price"]
    for row_menu1 in menu_category:
        for key, value in row_menu1['additional_fields'].items():
            if key not in fltr_list:
                fltr_list.append(key)
    return fltr_list


def input_filter(fltr_list2):
    """
    :param fltr_list2: список варіантів х-ки в рамках 1го фільтра
    :return: повертає 1 з введених команд reset, exit
     або якщо filter, то повертає вибраний параметр
    """
    while True:
        fltr = input('''Виберіть один з варіантів:
    filter - якщо хочете вибрати один з фільтрів;
    reset - якщо хочете повернутися до вибору категорії
    exit - вийти з програми
    >>     ''')
        if fltr == 'filter':
            print('Виберіть один з фільтрів:')
            for row_cat in fltr_list2:
                print(row_cat)
            fltr_l = category_input(fltr_list2)
            return fltr_l
            break
        elif fltr in ('reset', 'exit'):
            return fltr
            break
        else:
            print('Введіть один з фільтрів вище')


def add_fltr_menu(menu1, ch_fl, marker):
    """
    :param menu1: список словників зі всіма характеристиками, попередгьо відфільтровані
    :param ch_fl: заданий фільтр
    :param marker: назва х-ки по якій була остання фільтрація
    :return: нове меню - список словників
    """
    menu_add = list()
    for r in menu1:
        if marker == 'Price':
            if r[marker.lower()] == ch_fl:
                menu_add.append(r)
        else:
            if r['additional_fields'][marker] == ch_fl:
                menu_add.append(r)
    return menu_add


def fltr_choice_list(res_1, menu_1):
    """
    :param res_1: назва фільтру
    :param menu_1: список словників, база для фільтрування
    :return: повертає список назв бренду/діагоналі екрану тощо, при вибраному фільтрі
    """
    fltr_ch_list = list()
    for row_menu in menu_1:
        if res_1.lower() == 'price':
            if row_menu[res_1.lower()] not in fltr_ch_list:
                fltr_ch_list.append(row_menu[res_1.lower()])
        else:
            if row_menu['additional_fields'][res_1] not in fltr_ch_list:
                fltr_ch_list.append(row_menu['additional_fields'][res_1])
    return fltr_ch_list


def category_part():
    """
    :return: повртаэ назву категорії, яку вибрав користувач
    """
    category_list = category_lists()
    print(' Категорії товарів:')
    j = 0
    for i in category_list:
        j += 1
        print(f' {j}. {i}.')
    k = category_input(category_list)
    return k


def part_fltr(menu_def, res_delete1):
    """
    :param menu_def: список словників зі всіма характеристиками, попередгьо відфільтровані
    :param res_delete1: параметр з фыльтрів, який треба видалити, щоб не дублювати інформацію
    :return: список введених назв х-к
    """
    fltr_list1 = group_fltr(menu_def)
    if res_delete1:
        if res_delete1 in fltr_list1:
            fltr_list1.remove(res_delete1)
    res_name_fltr = input_filter(fltr_list1)
    return res_name_fltr


if __name__ == '__main__':
    catalog = load_dict()
    k = category_part()
    res_delete = []
    exit_marker = False
    menu = check_category()
    group_category(menu)
    while exit_marker is False:
        res = part_fltr(menu, res_delete)
        if res == 'reset':
            catalog = load_dict()
            k = category_part()
            menu = check_category()
            group_category(menu)
        elif res == 'exit':
            exit_marker = True
            print('Дякую, що завітали в наш e-shop. До зустрічі :)')
        else:
            fltr_ch_list_1 = fltr_choice_list(res, menu)
            print(f'В наявності: {fltr_ch_list_1}')
            ch_fltr = category_input(fltr_ch_list_1)
            menu2 = add_fltr_menu(menu, ch_fltr, res)
            group_category(menu2)
            fltr_ch_list_1.remove(ch_fltr)
            menu = menu2
            res_delete.append(res)
