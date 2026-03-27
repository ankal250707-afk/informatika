# TODO импортировать необходимые молули
import csv  # Для работы с CSV-файлами
import json  # Для работы с JSON-файлами
INPUT_FILENAME = "input.csv"  # Имя входного CSV-файла
OUTPUT_FILENAME = "output.json"  # Имя выходного JSON-файла
def task() -> None: # Создаем функцию task
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file: # Открываем файл в режиме чтения с кодировкой utf-8
        csv_reader = csv.DictReader(csv_file)  # Читаем файл, используя заголовки как ключи
        data = list(csv_reader)  # Преобразуем данные в список словарей
    # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file: # Открываем файл в режиме записи с кодировкой utf-8
        json.dump(data, json_file, indent=4, ensure_ascii=False) # преобразуем data в JSON, записываем JSON в файл json_file, форматируем вывод с отступами, ensure_ascii=False для поддержки кириллицы
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    task()
# Проверяем содержимое и выводим json-файл
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
