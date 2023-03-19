import os


def add_contact():
    first_name = input('Input first name: ')
    last_name = input('Input last name: ')
    phone = input('Input phone: ')
    contact = first_name + ' ' + last_name + ' ' + phone + '\n'
    file = open('file.txt', 'a', encoding='utf-8')
    file.write(contact)
    file.close()
    return contact


def find():
    f = input(
        'Введите фамилию, имя или номер телефона для поиска интересующего контакта: ').upper()
    lines = read_phonebook()
    cnt = 0
    lst = list()
    for line in lines:
        if f in line.upper():
            cnt += 1
            lst.append(line)
    if cnt == 0:
        return 0
    return lst


def read_phonebook():
    file = open('file.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    lst = []
    for line in lines:
        lst.append(line)
    file.close()
    return lst


def delete(st):
    if len(st) == 1:  # в случае, если найден 1 контакт
        lines = read_phonebook()
        file = open('file.txt', 'w', encoding='utf-8')
        for line in lines:
            if st[0] not in line:
                file.write(line)
        file.close()
    else:  # в случае, если найдено больше контактов
        value = get_int_input('Введите номер строки, которую хотите изменить: ')
        if value > len(st):
            return 0
        else:
            st = [st[value - 1]]
            delete(st)


def edit(st):
    if len(st) == 1:  # в случае, если найден 1 контакт
        lines = read_phonebook()
        file = open('file.txt', 'w', encoding='utf-8')
        for i in range(len(lines)):
            if st[0] in lines[i]:
                lines[i] = lines[i].replace(st[0], add_contact())
                file.write(lines[i])
            else:
                file.write(lines[i])
        file.close()
    else:  # в случае, если найдено больше контактов
        value = get_int_input('Введите номер строки, которую хотите изменить: ')
        if value > len(st):
            return 0
        else:
            st = [st[value - 1]]
            edit(st)


def press_any_key():
    if os.name == 'nt':
        os.system('pause')
    else:
        os.system('read -s -n 1 -p "Press any key to  continue ..."')


def get_int_input(st=''):
    while True:
        try:
            value = int(input(st))
            return value
        except ValueError:
            print('Invalid input. Please enter an integer.')
