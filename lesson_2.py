a = input('Введіть, будь ласка, число: ')
try:
    k = int(a) // 10
    if k == 0:
        print('')
    else:
        print(k)
except Exception:
    print('Ви ввели не число. Введіть, будь ласка, число')
