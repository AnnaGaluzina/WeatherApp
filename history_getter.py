import json


def history_recorder(data: dict):
    """
        Функция получает данные и записывает их в файл data.json, если они существуют.
        К существующим данным добавляет новые.
    """
    requests_history = history_reader()

    if data is not None:
        with open('data.json', 'w+') as file:
            if requests_history == '' or requests_history is None:
                requests_history = []

            if requests_history is not None:
                requests_history.append(data)
                file.write(json.dumps(requests_history, indent=0, ensure_ascii=True))


def history_reader() -> list:
    """
        Функция считывает данные из файла data.json и возвращает их в виде списка словарей.
    """
    try:
        with open("data.json", "r+") as file:
            data_from_file = json.load(file)
        return data_from_file
    except Exception:
        print('\nВозникла ошибка при получении данных.')


def history_cleaner():
    """
        Функция удаляет записи из файла с данными data.json.
    """
    with open('data.json', 'w') as file:
        file.write(json.dumps([], indent=0, ensure_ascii=False))
    print('\nИстория удалена.')
