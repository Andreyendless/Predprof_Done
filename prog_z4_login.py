import csv
import random

def create_login(fio):
    '''
    Функция создает логин пользователя по переданной строке с фамилией, именем и отчеством ученика

    Параметры:
    fio - входная строка, содержащая фамилию имя и отчество
    '''
    surname, name, patrynomic = fio.split()
    return f'{surname}_{name[0]}{patrynomic[0]}'

def create_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.choice(letters) for _ in range(8))
    return password


new_data = []
with open('students.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for student in data:
        student['login'] = create_login(student['Name'])
        student['password'] = create_password()
        new_data.append(student)

with open('students_password.csv', 'w', encoding='utf-8', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=['id','Name','titleProject_id','class','score','login','password'], delimiter=',')
    writer.writeheader()
    writer.writerows(new_data)