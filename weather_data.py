import requests
from datetime import datetime, timezone, timedelta
import geocoder
from typing import Any
from config import API_KEY, URL
from history_getter import history_recorder


def get_weather(city: str | None) -> dict[str: Any]:
    """
        Функция получает данные с веб-сервиса openweathermap по веденному пользователем названию города.
        Возвращает словарь с данными о погоде.
    """
    try:
        if not city:
            city = get_weather_by_location()

        response = requests.get(URL.format(city, API_KEY),
                                params={'units': 'metric', 'lang': 'ru'},
                                timeout=5,
                                )
        data = response.json()
        parsed_data = parse_weather_data(data)
        printing_weather_info(parsed_data)
        history_recorder(parsed_data)

        if response.json().get("cod") == "404":
            print(f'Город не найден.')

    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        print(f'Возникла проблема с соединением.')

    except requests.exceptions.HTTPError:
        print(f'Город не найден.')


def get_weather_by_location() -> str:
    """
        Функция определяет текущее местоположение пользователя и возвращает название города.
    """
    try:
        city = geocoder.ip('me').city
        return city
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        print('Не удалось определить ваше местоположение.')


def parse_weather_data(data: dict) -> dict:
    """
        Функция обрабатывает полученные данные и возвращает словарь необходимых для вывода данных.
        Если данные не были получены, то функция ничего не вернет.
    """
    if data is None:
        print(f'Данные не были получены.')

    try:
        time_shift = data["timezone"]
        current_time = data["dt"]
        time_zone = timezone(timedelta(seconds=time_shift))
        current_time = datetime.fromtimestamp(current_time, time_zone)

        city = data['name']
        weather_conditions = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        wind_speed = data['wind']['speed']

        weather_info_parsed = {
                'time': str(current_time),
                'city': str(city),
                'conditions': str(weather_conditions).capitalize(),
                'temperature': temperature,
                'feels_like': feels_like,
                'wind_speed': wind_speed
        }

        return weather_info_parsed

    except Exception:
        print(f'Возникла ошибка при получении данных.')


def printing_weather_info(weather_info_parsed: dict):
    """
        Функция получает словарь с нужными данными и составляет строку для вывода.
        Ничего не возвращает.
    """
    if weather_info_parsed is None:
        return None

    weather_info = f"""
            Текущее время: {weather_info_parsed['time']}
            Название города: {weather_info_parsed['city']}
            Погодные условия: {weather_info_parsed['conditions']}
            Текущая температура: {weather_info_parsed['temperature']} градусов по цельсию
            Ощущается как: {weather_info_parsed['feels_like']} градусов по цельсию
            Скорость ветра: {weather_info_parsed['wind_speed']} м/c
            """
    print(weather_info)


def display_history_list(list_history: list):
    """
    Функция выводит историю запросов.
    """
    for weather_data in list_history:
        printing_weather_info(weather_data)
