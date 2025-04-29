moja_lista_na_sok= []
print(moja_lista_na_sok)


    def add_user(users_data: list)->None:
    new_name = input('podaj lokalizacje uzykownika  ')
    new_location =input('podaj lokalizacje uzykownika  ')
    new_numbers =int(input('podaj numer postow') )
    users_data.append({"name":new_name,"Location":new_location,"posty":new_numbers})

 add_user(moja_lista_na_sok)

users = [
    {"name": "Beata", "Location": "Lublin", "posts": 500},
]


def remove_user(users_data: list) -> None:
    uzytkownik_do_usuneicia = input('podaj uzytkownika do usuniecia')

    for user in users_data:

        if user['name'] == uzytkownik_do_usuneicia:
            users_data.remove(user)


print(users)

print(moja_lista_na_sok)

