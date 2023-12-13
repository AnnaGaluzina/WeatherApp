from weather_data import get_weather, display_history_list
from history_getter import history_reader, history_cleaner

MENU = """
1. Узнать погоду по названию города
2. Узнать погоду по текущему местоположению
3. Узнать историю запросов
4. Очистить историю запросов
5. Выход
"""


def main():
    """
        Функция выводит список доступных команд и предлагает пользователю ввести одну из них.
        Пользователь может выбрать одну из следующих команд:
            -1: Узнать погоду по названию города
            -2: Узнать погоду по текущему местоположению
            -3: Узнать историю запросов
            -4: Очистить историю запросов
            -5: Выход
        После ввода одной из команд программа запускает соответствующую функцию.
    """
    while True:
        print(MENU)
        action = input('Выберите действие: ').strip()

        if action == '1':
            city = input('\nВведите название города: ').strip()
            get_weather(city)

        elif action == '2':
            get_weather(None)

        elif action == '3':
            while True:
                number_of_records = input(
                    'Введите число записей, которое необходимо вывести к просмотру: '
                )
                if number_of_records.isdigit():
                    request_history = history_reader()
                    if isinstance(request_history, type(None)):
                        print('Записей нет.')
                        break

                    request_history.reverse()

                    if int(number_of_records) >= len(request_history):
                        display_history_list(request_history)
                    else:
                        display_history_list(
                            request_history[:int(number_of_records)]
                        )

                    print(f'\nВсего в архиве {len(request_history)} записей.')
                    print(
                        f'Показано {min(len(request_history), int(number_of_records))} записей.'
                    )

                    break
                else:
                    print('Вы ввели не корректную запись, попробуйте снова.')

        elif action == '4':
            history_cleaner()

        elif action == '5':
            break

        else:
            print('Неизвестная команда. Пожалуйста, выберите из предложенного списка.')


if __name__ == "__main__":
    main()
