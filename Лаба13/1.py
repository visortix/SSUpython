import csv
import json


def csv_to_json(csv_file_path, json_file_path):  # Ustymenko
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Файл {csv_file_path} успішно конвертовано у {json_file_path}")
    except FileNotFoundError:
        print(f"Файл {csv_file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


# Створення .csv файлу з кількома рядками:
with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:  # Ustymenko
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Ivan', 25, 'Kyiv'])
    writer.writerow(['Maria', 20, 'Lviv'])

# Конвертація .csv у .json:
csv_to_json('data.csv', 'data.json')
