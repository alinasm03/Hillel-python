def field_input(name):
    while True:
        x = input(f'Введіть {name}: ')
        marker_x = False
        for i in x:
            try:
                t = int(i)
                marker_x = True
                break
            except Exception:
                continue
        if marker_x is True:
            print('Введіть, будь ласка, НЕ число!')
        else:
            return x


name_recipient = field_input("Ім'я одержувача")
surname_recipient = field_input('Прізвище одержувача')
name_sender = field_input("Ім'я відправика")
surname_sender = field_input('Прізвище відправника')
post_sender = field_input('Посада відправника')
print(f'''
    Dear {name_recipient} {surname_recipient}, \n
    We are lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Vestibulum in faucibus massa. 
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. \
In vel est a tortor tempor luctus a. \n
    ________________
    {name_sender} {surname_sender}
    {post_sender}''')
