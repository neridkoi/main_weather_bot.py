from config import ju_weather
import requests

def get_weather(city, ju_weather):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={ju_weather}&units=metric")
        data = r.json()
        #pprint(data)
        city = data['name']
        cur_temp = data['main']['temp']
        humid = data['main']['humidity']
        pres = data['main']['pressure']*0.75
        descript = data['weather'][0]['description']
        wind = data['wind']['speed']
        print(f"Погода в {city}:\nТемпература: {cur_temp}\nВлажность: {humid}\nДавление: {pres}\nОписание: {descript}\nВетер: {wind}")
        print()
    except Exception as ex:
        print(ex)
        print('Проверьте название города')
def main():
    #city=input("Введите название города")
    city1='batumi'
    city2 = 'mariupol'
    get_weather(city1, ju_weather)
    get_weather(city2, ju_weather)

if __name__ == '__main__':
    main()