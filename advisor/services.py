import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуй позже>'

def what_temperature(weather):    
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуй позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
        if temperature < -10:
            return 'Холодно. Не забудь взять шапку и перчатки.'
        elif temperature >= -10 and temperature < 0:
            return 'Холодновато. Шапка не помешает.'
        elif temperature >= 0 and temperature < 10:
            return 'Достаточно тепло для прогулок.'
        elif temperature >= 10 and temperature < 25:
            return 'Хорошая температура для прогулок.'
        else:
            return 'Жарко. Не забудь солнцезащитный крем.'                   
    except ValueError:
        return 'Не могу узнать погоду. Реши сам, что взять с собой в дорогу.'
