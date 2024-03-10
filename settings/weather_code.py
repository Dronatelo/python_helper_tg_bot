import requests
import datetime

def get_weather(city):
    tokken = "*"
    code_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        w = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tokken}&units=metric')

        data_weather = w.json()
        
        city = data_weather['name']
        temperature = data_weather['main']["temp"]
        
        w_d = data_weather["weather"][0]["main"]
        if w_d in code_smile:
            wd = code_smile[w_d]
        else:
            wd = "Странная погода. Не могу понять..."

        humidity = data_weather['main']["humidity"]
        pressure = data_weather['main']["pressure"]
        wind = data_weather['wind']["speed"]
        s_t = datetime.datetime.fromtimestamp(data_weather['sys']["sunrise"])
        se_t = datetime.datetime.fromtimestamp(data_weather['sys']["sunset"])
        l_d_e = datetime.datetime.fromtimestamp(data_weather['sys']["sunset"]) - datetime.datetime.fromtimestamp(data_weather['sys']["sunrise"])
        
        return f"🌎{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}🌎\n🌇Погода в городе: {city}🌃\n🌡Температура: {temperature}C° {wd}\n💦Влажность: {humidity}%💦\n🎚Давление: {pressure} мм.рт.ст🎚\n🌬Ветер: {wind} м/c🌬\n🌤Восход солнца: {s_t}\n🌙Закат Солнца: {se_t}\n☀Продолжительность дня: {l_d_e}"
    except Exception as ex:
        print("error weather.py \ncode error: ", ex)
        return "❗Проверьте название городa❗"
