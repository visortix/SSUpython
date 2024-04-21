def write_data(filename, stud_name, answer, question, flag):
    try:
        # Відкриття файлу для допису (створення, якщо не існує)
        with open(filename, "a", encoding="utf-8") as file:  # Змінено режим на "a"
            # Запис прізвища та питання у файл
            file.write(f"--- {stud_name} ---\n")
            if flag == 1:
                file.write(f"{answer}\n")
            file.write(f"{question}\n")
    except OSError as error:
        print(f"Помилка при роботі з файлом: {error}")

filename = "python_questions.txt"

# Повне очищення файлу для перезапису
try:
    with open(filename, "r+") as file:
        file.truncate(0)
except OSError as error:
    print(f"Помилка при роботі з файлом: {error}")

flag = 0

student_name = "Ustymenko"
answer = " "
question = "Як перевірити тип даних змінної в Python?"

write_data(filename, student_name, answer, question, flag)

print(f"Файл '{filename}' створено та заповнено питанням.")

# Milanovych Dmytro
flag = 1  # Для допису рядка answer (опціонально)

student_name = "Milanovych"
answer = "Потрібно використати функцію type()"
question = "Які методи використовуються для зчитування вмісту файлу текстового формату в Python?"

write_data(filename, student_name, answer, question, flag)

print(f"Файл '{filename}' заповнено відповіддю та новим питанням.")
