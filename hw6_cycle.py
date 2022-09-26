def input_function():
    print('''Введіть, будь ласка, 
    1. Число 
    2. або sum (щоб зупинити роботи програми та підрахувати суму чисел)!
    ''')
    x = 0
    sum1 = 0
    while x != 'sum':
        x = input()
        try:
            if type(float(x)) == float:
                sum1 += float(x)
        except Exception:
            if x != 'sum':
                print('Введіть, будь ласка, число або sum!')
            else:
                return sum1


n = input_function()
print(n)
