from gettext import find
import model as processing
import view
import os


def run():
    view.greeting()
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        view.menu()
        choice = processing.get_int_input()
        if choice == 1:
            a = processing.find()
            if a == 0:
                view.empty_result()
                processing.press_any_key()

            else:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(*a, sep='')
                    view.find_menu()
                    find_choice = processing.get_int_input()
                    if find_choice == 1:
                        result = processing.edit(a)
                        if result == 0:
                            view.error()
                            processing.press_any_key()
                        break
                    elif find_choice == 2:
                        result = processing.delete(a)
                        if result == 0:
                            view.error()
                            processing.press_any_key()
                        break
                    elif find_choice == 3:
                        break
                    else:
                        print('Input error')
                        processing.press_any_key()

        elif choice == 2:
            processing.add_contact()
        elif choice == 3:
            view.show_phonebook()
            processing.press_any_key()

        elif choice == 4:
            break
        else:
            print('Input error')
            processing.press_any_key()
