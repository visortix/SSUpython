def first_edit(text):
    content_split = text.split()  # Розділення тексту на масив слів
    letters = 0
    text_new_lines_size = []
    for word in content_split:
        letters += len(word)
        text_new_lines_size.append(word)
        if letters > 45:
            text_new_lines_size.append('\n')
            letters = 0
    return ' '.join(text_new_lines_size)  # Збирання масиву в текст


def second_edit(text):
    content_split = text.split()

    # Видалення префікса (removeprefix)
    text_new_lines_size = [word.removeprefix("wa") if word.startswith("wa") else word for word in content_split]

    # Видалення суфікса (removesuffix)
    text_new_lines_size = [word.removesuffix("ed") if word.endswith("ed") else word for word in text_new_lines_size]

    # Додавання слова (__add__)
    addWord = " next"
    text_new_lines_size = [word.__add__(addWord) if word.endswith("and") else word for word in text_new_lines_size]

    return ' '.join(text_new_lines_size)


with open('text.txt', 'r', encoding='utf') as rf:
    print(f'file: {rf.name}')

    # Читання з файлу
    rf_content = rf.read()
    print(f'\nText:\n{rf_content}')

#Перша ітерація Dmytro Ustymenko
# Перенесення на новий рядок
result = first_edit(rf_content)

# Подальша робота print(help(str))
result = result.replace('\n ', ' \n')  # Заміна символів
result = result.replace(' had', '\'d')

# Виведення результатів
print(f'\nFirst iteration text:\n{result}')

#Друга ітерація Dmytro Milanovych
#Функції для використання: (removeprefix, removesuffix, __add__)
result = second_edit(rf_content)
print(f'\nSecond iteration text:\n{result}')

#Третя ітерація
#Функції для використання: ( )

# Виведення результатів
print(f'\nThird iteration text:\n{result}')

#Четверта ітерація
#Функції для використання: ( )

# Виведення результатів
print(f'\nFourth iteration text:\n{result}')

# Збереження у новий файл
with open('text_result.txt', 'w', encoding='utf') as wf:
    wf.write(result)
