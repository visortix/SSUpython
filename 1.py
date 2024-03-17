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

    #Видалення префікса (removeprefix)
    text_new_lines_size = [word.removeprefix("wa") if word.startswith("wa") else word for word in content_split]

    #Видалення суфікса (removesuffix)
    text_new_lines_size = [word.removesuffix("ed") if word.endswith("ed") else word for word in text_new_lines_size]

    #Додавання слова (__add__)
    addWord = " next"
    text_new_lines_size = [word.__add__(addWord) if word.endswith("and") else word for word in text_new_lines_size]

    #Перенесення рядків
    letters = 0
    for i, word in enumerate(text_new_lines_size):
        letters += len(word)
        if letters > 45:
            text_new_lines_size[i - 1] += '\n'
            letters = len(word)

    return ' '.join(text_new_lines_size)

def third_edit(text):
    content_split = text.split()

    # Метод upper
    text_new_lines_size = [word.upper() for word in content_split]

    # Метод title
    text_new_lines_size = [word.title() for word in text_new_lines_size]

    # Метод swapcase
    text_new_lines_size = [word.swapcase() for word in text_new_lines_size]

    letters = 0
    for i, word in enumerate(text_new_lines_size):
        letters += len(word)
        if letters > 45:
            text_new_lines_size[i - 1] += '\n'
            letters = len(word)

    return ' '.join(text_new_lines_size)

def fourth_edit(text):
    content_split = text.split()

    # Метод capitalize
    text_new_lines_size = [word.capitalize() for word in content_split]

    # Метод replace
    text_new_lines_size = [word.replace('y', 'z') for word in text_new_lines_size]

    # Метод count
    count = sum(word.count('t') for word in text_new_lines_size)
    print("Кількість 't' у тексті:", count)

    letters = 0
    for i, word in enumerate(text_new_lines_size):
        letters += len(word)
        if letters > 45:
            text_new_lines_size[i - 1] += '\n'
            letters = len(word)

    return ' '.join(text_new_lines_size)

#Читання з файлу
with open('text.txt', 'r', encoding='utf') as rf:
    print(f'file: {rf.name}')
    rf_content = rf.read()
    print(f'\nText:\n{rf_content}')

#Перша ітерація Dmytro Ustymenko
# Перенесення на новий рядок
result = first_edit(rf_content)
result = result.replace('\n ', ' \n')  # Заміна символів
result = result.replace(' had', '\'d')

# Виведення результатів
print(f'\nFirst iteration text:\n{result}')

#Друга ітерація Dmytro Milanovych
#Функції для використання: (removeprefix, removesuffix, __add__)
result = second_edit(rf_content)
result = result.replace('\n ', ' \n')
print(f'\nSecond iteration text:\n{result}')

#Третя ітерація Chuchlib Evgeniy
#Функції для використання: (upper, title, swapcase)
result = third_edit(rf_content)
result = result.replace('\n ', ' \n')

# Виведення результатів
print(f'\nThird iteration text:\n{result}')

#Четверта ітерація Radko Vitalii
#Функції для використання: (capitalize, replace, count)
result = fourth_edit(rf_content)
result = result.replace('\n ', ' \n')

# Виведення результатів
print(f'\nFourth iteration text:\n{result}')

# Збереження у новий файл
with open('text_result.txt', 'w', encoding='utf') as wf:
    wf.write(result)