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
    f = input().upper()
    lines = reed_phonebook()
    cnt = 0
    for line in lines:
        if f in line.upper():
            cnt += 1
            return line
    if cnt == 0:
        return 'error find contact'


def reed_phonebook():
    file = open('phonebook/file.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    lst = []
    for line in lines:
        lst.append(line)
    file.close()
    return lst

def delete(st):
    lines = reed_phonebook()
    file = open('phonebook/file.txt', 'w', encoding='utf-8')
    for line in lines:
        if st not in line:
            file.write(line)
    file.close()

def edit(st):
    lines = reed_phonebook()
    file = open('phonebook/file.txt', 'w', encoding='utf-8')
    for i in range(len(lines)):
        if st in lines[i]:
            lines[i] = lines[i].replace(st, add_contact())
            file.write(lines[i])
        else:
            file.write(lines[i])
    file.close()

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