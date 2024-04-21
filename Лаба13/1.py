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

def json_to_csv(json_file_path, csv_file_path):  # Milanovych
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Файл {json_file_path} успішно конвертовано у {csv_file_path}")
    except FileNotFoundError:
        print(f"Файл {json_file_path} не знайдено.")
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

# Milanovych
# Додавання даних до файлу .json

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)  # Завантаження вмісту файлу JSON

# Додавання нового словника (рядка) до списку існуючих даних
data.append({"Name": "Andriy", "Age": 18, "City": "Sumy"})
data.append({"Name": "Anna", "Age": 23, "City": "Poltava"})

# Збереження оновленого списку у файл JSON
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)
print(f"Дані успішно додано до файлу data.json")


# Конвертація
json_to_csv('data.json', 'data.csv')
