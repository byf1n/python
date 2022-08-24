# --------1---------
# try:
#     with open('emails.txt') as emails_file, open('result.txt','w') as result_file:
#         for line in emails_file:
#             emails = line.strip().split('\t')[-1]
#             if emails.split('@')[-1] == 'gmail.com':
#                 print(emails, file=result_file)
# except Exception as error:
#     print(error)
#############################

# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
import json
from typing import TypedDict

NoteType = TypedDict('NoteType', {'purchase': str, 'cost': int})


class Note:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__notes: list[NoteType] = []
        try:
            with open(self.__file_name) as file:
                self.__notes: list[NoteType] = json.load(file)
        except:
            pass

    def add(self):
        try:
            with open(self.__file_name, 'w') as file:
                purchase = input('name: ')
                cost = ''

                while not cost.isdigit():
                    cost = input('price: ')

                self.__notes.append({'purchase': purchase, 'cost': int(cost)})
                json.dump(self.__notes, file)
        except:
            print('ban')

    def all(self):
        if not self.__notes:
            print('nema pokupok!!')
        return

        for item in self.__notes:
            print(item)

    def sum(self):
        summ = sum([item['cost'] for item in self.__notes])

        print(f'{summ=}')

    def most_expensive(self):
        print(max(self.__notes, key=lambda item: item['cost']))

    def find_by_name(self):
        find = input('name: ')

        for item in self.__notes:
            if item['purchase'].lower() == find.lower():
                print(item)
                return
        print('??????')


note = Note('lalal')

while True:
    print('1 - add')
    print('2 - show all')
    print('3 - summ')
    print('4 - most expensive')
    print('5 - find by name')
    print('0 - exit')

    choise = input('enter a num: ')

    match choise:
        case '1':
            note.add()
        case '2':
            note.all()
        case '3':
            note.sum()
        case '4':
            note.most_expensive()
        case '5':
            note.find_by_name()
        case '0':
            break






