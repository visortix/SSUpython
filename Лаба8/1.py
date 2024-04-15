def print_data(vocabulary):  # Ustymenko Dmytro
    for id in students_data:
        print(students_data[id])


def add_data(vocabulary):  # Ustymenko Dmytro
    new_id = len(vocabulary) + 1
    new_student_data = {
        new_id: {
            "group": '',
            "full_name": "",
            "course": -1,
            "subjects": {
                "Math": -1,
                "Physics": -1,
                "IT": -1,
            }
        }
    }

    for data in new_student_data[new_id]:
        if data == 'subjects':
            for subject in new_student_data[new_id][data]:
                new_student_data[new_id][data][subject] = int(input(f'Enter {subject}: '))
            continue
        new_student_data[new_id][data] = input(f'Enter {data}: ')

    students_data.update(new_student_data)
    return students_data


students_data = {  # Ustymenko Dmytro
    1: {
        "group": 'IN-23',
        "full_name": "Іванов Іван Іванович",
        "course": 2,
        "subjects": {
            "Math": 5,
            "Physics": 4,
            "IT": 5,
        }
    },
    2: {
        "group": 'IN-21',
        "full_name": "Петренко Петро Петрович",
        "course": 2,
        "subjects": {
            "Math": 4,
            "Physics": 5,
            "IT": 3,
        }
    }
}

print_data(students_data)
students_data = add_data(students_data)
print_data(students_data)
# некст видалення
