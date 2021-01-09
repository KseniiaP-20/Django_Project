from django.shortcuts import render
from city.models import city_db
from advisor.models import friends_db
from advisor.services import what_weather, what_temperature, what_conclusion


def index(request):
    cities = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    selected_city = ''
    city_weather2 = ''
    conclusion = ''

    for friend in friends_db:
        friends += (f'<input type="radio" name="friend"'
                   f' required value="{friend}">{friend}<br>')

    for i in range(len(city_db)):
        city_form = (f'<input type="radio" name="city" required'
                    f' value="{city_db[i]["name"]}">{city_db[i]["name"]}')

        city_link = f'<a href="city/{i}/">О городе</a>'
        cities += f'{city_form} | {city_link} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        selected_city = request.POST['city']
        
        city = friends_db[selected_friend]
        weather = what_weather(city)
        weather2 = what_weather(selected_city)
        parsed_temperature = what_temperature(weather2)
        conclusion = what_conclusion(parsed_temperature)
        friend_output = (f'{selected_friend}, тебе прислали приглашение в город '
                 f'{selected_city}!')
        city_weather = f'В твоем городе {city} сейчас {weather}'
        city_weather2 = f'В городе {selected_city} сейчас {weather2}'

    context = {
        'cities': cities,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
        'conclusion': conclusion,
        'city_weather2': city_weather2
    }
    return render(request, 'homepage/index.html', context)
