from init.controller import get_user_info, add_user, remove_user,
from init.model import users

def main():

    while True:
        print("==========MENU=================")
        print("0 - zamknij aplikacje")
        print("1 - wyświetl co u znajomych")
        print("2 - dodaj nowego użytkownika")
        print("3 - usuń użytkownika")
        print("4 - edytuj użytkownika")
        print("==============MENU===================")

        choice = input("wybierz opcje menu")
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': add_user(users)



if _name_ == "_main_":
    main()

