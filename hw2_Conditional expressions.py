a = input('Введіть, будь ласка, число: ')
try:
    if float(a) <= -500:
        print('Число дорівнює або менше ніж -500')
    elif -500 < float(a) <= -100:
        print('Дорівнює або менше ніж -100, але більше -500')
    elif -100 < float(a) < 0:
        print('Менше ніж 0, але більше -100')
    elif 0 <= float(a) < 100:
        print('Дорівнює або більше ніж 0, але менше 100')
    elif 100 <= float(a) < 500:
        print('Дорівнює або більше ніж 100, але менше 500')
    else:
        print('Дорівнює або більше ніж 500')
except Exception:
    print('Ви ввели не число. Введіть, будь ласка, число')