

users=[
{"name":"Beata","Location":"Lublin","posts":500},
{"name":"Michal","Location":"Krasnystaw","posts":420},
{"name":"Ksavier","Location":"Grudziac","posts":690},
{"name":"Damian","Location":"Kraków","posts":699},

]



Twoj znaomy z opublikowal tyle i tyle postow
for user in users:
    print(f"twoj zajomy {user['name']} , z:{user['location']} , opublikowal :{user['posts'])
    
def get_user_info(users_data: list)->None:

    get_user_info(users)