from os import name


def greeting():
    print('\n***********************************\nДобро пожаловать в записную книжку!\n***********************************\n')
    print(input('Нажмите любую клавишу для продолжения...'))


def menu():
    print('\n********************************\n           Phonebook\n********************************\n\n 1. Find\n 2. Add contact\n 3. Show phonebook\n 4. Quit\n')


def empty_result():
    print('\nКонтакт с заданными данными не найден. Хотите добавить данный контакт? 1 - "Да", 0 - "Нет".\n')


def error():
    print('\nError occured while trying to process your input. Please, try again.\n')


def show_phonebook():
    path = 'file.txt'
    try:
        file = open(path, 'r')
        print('\n********************************\n')
        for line in file:
            print(line)
        file.close()
        print('\n********************************\n')
    except FileNotFoundError:
        file = open(path, 'w+')
        print('\n********************************\n')
        for line in file:
            print(line)
        file.close()
        print('\n********************************\n')


def find_menu():
    print('********************************\n           Choice\n********************************\n\n 1. Edit contact\n 2. Delete contact\n 3. Return menu\n')
