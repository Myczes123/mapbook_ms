def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości: {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imię nowego uzytkownika: ')
    new_location = input('podaj lokalizację uzytkownika: ')
    new_posts = int(input('podaj liczbę postów nowego uzytkownika: '))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts}, )

def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)


def upadte_users(users_data: list) -> None:
    uzytkownik_do_edycji = input('podaj uzytkownika do edycji:')
    for user in users_data:
        if user['name'] == uzytkownik_do_edycji:
            user['name'] = input('podaj nowe imie uzytkownika')
            user['location'] = input('podaj nowa lokalizacje  uzytkownika')
            user['posts'] = int(input('podaj nowa liczbe postow'))

            users = [
                {"name": "Beata", "Location": "Lublin", "posts": 500},
                {"name": "Michal", "Location": "Krasnystaw", "posts": 420},
                {"name": "Ksavier", "Location": "Grudziąc", "posts": 690},
                {"name": "Damian", "Location": "Kraków", "posts": 699},
            ]

            from bs4 import BeautifulSoup

            # https://pl.wikipedia.org/wiki/Lublin
            def get_cordinates(city: str) -> list:

                url = f'https://pl.wikipedia.org/wiki/{city}'
                response = requests.get(url).text

                response_html = BeautifulSoup(response, 'html.parser')
                longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
                latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
                return [longitude, latitude]

            map = folium.Map(location=(52.23, 21.00), zoom_start=6)
            for user in users:
                cordinates = get_cordinates(user['location'])
            import requests
            import folium
            folium.Marker(
                location=(52.23, 21.00)
            popup = (f"Twc"
                     f""
                     ój znajomy {user['name']}, z miejscowości: {user['location']} opublikował {user['posts']} postów")){user[name]}').add_to(map)
                     map.save('mapa.html')





