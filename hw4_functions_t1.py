def number_input(name: str) -> int:
    while True:
        x = input(f'Введіть, будь ласка, {name}: ')
        try:
            x = int(x)
        except Exception:
            print('Ви ввели не число або не ціле число. Введіть, будь ласка, ціле число!')
            continue
        if x >= 0 or (x < 0 and name == 'число'):
            return x
        else:
            print('Ви ввели не додатнє число. Введіть, будь ласка, число більше 0!')


def number_exist(number: int, count_cut_off: int) -> bool:
    if (len(str(number)) >= count_cut_off and number >= 0)\
            or (len(str(number)) - 1 > count_cut_off and number < 0):
        return True
    else:
        return False


def number_cut_off(number: int, count_cut_off: int):
    residual = abs(number) // 10**count_cut_off
    if residual == 0:
        if number == count_cut_off == 0:
            print(0)
        else:
            print('')
    elif residual != 0 and number < 0:
        print(-residual)
    else:
        print(residual)


number = number_input('число')
count_cut_off = number_input('кількість цифр, на які треба обрізати число')
if number_exist(number, count_cut_off):
    number_cut_off(number, count_cut_off)
else:
    print('')
