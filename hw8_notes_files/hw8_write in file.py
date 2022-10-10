import json
import os


def call_input():
    """
       Ф-я для введення команд:
            додавання нотаток, сортування, вивід в хронологічному порядку,
            зчитування з файла та зберігання в файл, а також його очистка.
       :param: список словників, note::str - нотатка, length::int - довжина нотатки
       :return: результат ф-й залежно від введених команд
    """
    end = False
    dict_note = []
    dict_note_input = []
    note_input_part = []
    while not end:
        call = input("Введіть, будь ласка, одну з команд: ")
        if call == 'add':
            add_note(note_input_part)
            if dict_note:
                dict_note_input += note_input_part
            else:
                dict_note_input = note_input_part
            dict_note = dict_note + note_input_part
            note_input_part = []
        elif call == 'earliest':
            print("Від найранішої до найпізнішої: ")
            for i in earliest_note(dict_note):
                print(i)
        elif call == 'latest':
            print("Від найпізнішої до найранішої: ")
            for i in latest_note(dict_note):
                print(i)
        elif call == 'longest':
            print("Від найдовшої до найкоротшої: ")
            for i in longest_note(dict_note):
                print(i)
        elif call == 'shortest':
            print("Від найкоротшої до найдовшої: ")
            for i in shortest_note(dict_note):
                print(i)
        elif call == 'save':
            save_note(dict_note)
            dict_note_input = []
            print("Нотатки збережено")
        elif call == 'load':
            dict_2 = {}
            list_keys = []
            notes = load_note(dict_note)
            if notes:
                for i in notes:
                    dict_2[i['note']] = i['length']
                    list_keys = list(dict_2.keys())
                # якщо файл з нотатками існує, то злити вміст файла з ще не збереженими даними
                dict_note = notes + dict_note_input
            else:
                list_keys = []
            print(list_keys)
        elif call == 'clear':
            clear_note()
            print('Всі нотатки разом з файлом видалені')
            dict_note = []
            dict_note_input = []
        elif call == 'exit':
            end = True
            print('Робота програми завершена. Дякую:)')
        else:
            print('Введіть правильну команду')
        print('')


def add_note(dict_note):
    note = input('Введіть нотатку: ')
    dict_notes = {'note': note,
                  'length': len(note)}
    dict_note.append(dict_notes)


def earliest_note(dict_note):
    key = []
    for i in dict_note:
        key.append(i['note'])
    return key


def latest_note(dict_note):
    key = []
    for i in dict_note:
        key.append(i['note'])
    key.reverse()
    return key


def longest_note(dict_note):
    dict_2 = {}
    for i in dict_note:
        dict_2[i['note']] = i['length']
    sorted_note = [i[0] for i in sorted(dict_2.items(), key=lambda x: x[1], reverse=True)]
    return sorted_note


def shortest_note(dict_note):
    dict_2 = {}
    for i in dict_note:
        dict_2[i['note']] = i['length']
    sorted_note = [i[0] for i in sorted(dict_2.items(), key=lambda x: x[1], reverse=False)]
    return sorted_note


def load_note(notes: list):
    """
    Ф-я зчитує з файла список словників:
    1. Якщо файла з нотатками не існує - повертає пустий список
    2. Якщо файл є - повертає список словників з json-файлу
    """
    file = 'hw_8_notes.json'
    if os.path.isfile(file):
        with open(file, mode='r') as f:
            note = json.load(open(file))
            notes = note['notes']
    else:
        notes = []
    return notes


def save_note(dict_note: dict):
    """
    Ф-я зберігає список введених словників dict_note в json-файл
    :param dict_note: нотатки, які ввів користувач, будуть збережені
    """
    file = 'hw_8_notes.json'
    if os.path.isfile(file):
        notes2 = dict_note
        with open(file, mode='w') as outfile:
            json.dump({"notes": notes2}, outfile, indent=4)
    else:
        json.dump(dict(notes=dict_note), open(file, mode='w'), indent=4)


def clear_note():
    """
    Ф-я затирає всі дані в файлі та видаляє сам файл
    """
    file = 'hw_8_notes.json'
    if os.path.isfile(file):
        os.remove(file)


print('''
    Команди:
add - додати нотатку;
load - завантажити нотатки з файлу;
save - зберегти нотатки в файл;
clear - очистити файл від нотаток;
exit - завершити роботу програми;
earliest - виводить нотатки від найранішої до найпізнішої;
latest - виводить нотатки від найпізнішої до найранішої;
longest - виводить нотатки від найдовшої до найкоротшої;
shortest - виводить нотатки від найкоротшої до найдовшої.
''')

call_input()
