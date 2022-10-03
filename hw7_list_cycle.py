def call_input():
    end = False
    while not end:
        call = input('Введіть, будь ласка, одну з команд: ')
        if call == 'add':
            add_note()
        elif call == 'earliest':
            print('Від найранішої до найпізнішої:')
            for i in earliest_note():
                print(i)
        elif call == 'latest':
            print('Від найпізнішої до найранішої:')
            for i in latest_note():
                print(i)
        elif call == 'longest':
            print('Від найдовшої до найкоротшої:')
            for i in longest_note():
                print(i)
        elif call == 'shortest':
            print('Від найкоротшої до найдовшої:')
            for i in shortest_note():
                print(i)
        elif call == 'end':
            end = True
            print('Робота програми завершена. Дякую:)')
        else:
            print('Введіть правильну команду')
        print('')

dict_note: dict['note', 'lenght'] = {}


def add_note():
    note = input('Введіть нотатку: ')
    dict_note[note] = len(note)
    return dict_note


def earliest_note():
    key = list(dict_note.keys())
    return key


def latest_note():
    key = list(dict_note.keys())
    key.reverse()
    return key


def longest_note():
    sorted_note = [i for i in sorted(dict_note.items(), key=lambda x: x[1], reverse=True)]
    keys_count = len(dict_note.values())
    l = list(sorted_note)
    l1 = []
    for j in range(keys_count):
        l1.append(l[j][0])
    return l1


def shortest_note():
    sorted_note = [i for i in sorted(dict_note.items(), key=lambda x: x[1], reverse=False)]
    keys_count = len(dict_note.values())
    l = list(sorted_note)
    l1 = []
    for j in range(keys_count):
        l1.append(l[j][0])
    return l1


print('''
    Команди:
add - додати нотатку;
earliest - виводить нотатки від найранішої до найпізнішої;
latest - виводить нотатки від найпізнішої до найранішої;
longest - виводить нотатки від найдовшої до найкоротшої;
shortest - виводить нотатки від найкоротшої до найдовшої.
''')


call_input()
