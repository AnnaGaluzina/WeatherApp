# Приложение Погода
С помощью этого консольного приложения пользователь может получить информацию о погоде по названию города и по его текущему местоположению.

Данные о погоде запрашиваются с веб-сервиса openweathermap при помощи библиотеки requests по названию города, которое вводит пользователь, или по его местоположению, которое определяется при помощи библиотеки geocoder.

Текущее время определяется на основании данных из openweathermap.

История запросов хранится в файле json.

Реализация интерфейса консольная.
Пользователь может выбрать одну из следующих команд:
 - 1: Узнать погоду по названию города
 - 2: Узнать погоду по текущему местоположению
 - 3: Узнать историю запросов 
 - 4: Очистить историю запросов 
 - 5: Выход
 
Информация будет предоставлена в виде:
```example
Текущее время: 2023-12-13 20:12:22+03:00
Название города: Санкт-Петербург
Погодные условия: Небольшой снег
Текущая температура: -1.91 градусов по Цельсию
Ощущается как: -7.31 градусов по Цельсию
Скорость ветра: 5 м/c
```
# Установка ПО для работы приложения:
1. Установите интерпретатор python версии 3.11.6 или выше
2. Скачайте репозиторий
3. Создайте виртуальное окружение c помощью команды:
    ```bash 
    python -m venv {venv name}
    ```
4. Активируйте его для Windows с помощью команды:
    ```bash 
    venv\Scripts\activate.bat
    ```
    Или для MacOS и Linux с помощью команды:
     ```bash 
    source venv/bin/activate
    ```
5. Установите необходимые библиотеки из файла requirements.txt с помощью команды:
    ```bash 
    pip install -r requirements.txt
    ```
6. Введите команду в консоли для запуска приложения:
    ```bash 
    python main.py
   ```