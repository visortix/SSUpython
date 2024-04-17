filename = "python_questions.txt"

student_name = "Ustymenko"
question = "Як перевірити тип даних змінної в Python?"

try:
    # Відкриття файлу для запису (створення, якщо не існує)
    with open(filename, "w", encoding="utf-8") as file:
        # Запис прізвища та питання у файл
        file.write(f"--- {student_name} ---\n")
        file.write(f"{question}\n")
except OSError as error:
    print(f"Помилка при роботі з файлом: {error}")

print(f"Файл '{filename}' створено та заповнено питанням.")