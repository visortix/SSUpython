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


with open('text.txt', 'r', encoding='utf') as rf:
    print(f'file: {rf.name}')
    # Читання з файлу
    rf_content = rf.read()

# Перенесення на новий рядок
result = first_edit(rf_content)
print(f'\nText:\n{result}')

# Подальша робота print(help(str))
result = result.replace('\n ', ' \n')  # Заміна символів
result = result.replace(' had', '\'d')
### ^ Dmytro Ustymenko ###

#NEXT-># removeprefix, removesuffix, __add__

# Виведення результатів
print(f'\nFinal text:\n{result}')

# Збереження у новий файл
with open('text_result.txt', 'w', encoding='utf') as wf:
    wf.write(result)
