import csv

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for i in range(len(reader)):
        cursor = reader[i]
        cursor_score = int(cursor['score'] if cursor['score']!='None' else 0)
        pos = i
        while pos > 0 and int(reader[pos-1]['score'] if reader[pos-1]['score']!='None' else 0)\
                < cursor_score:
            reader[pos] = reader[pos-1]
            pos -= 1
        reader[pos] = cursor
    id_input = input()
    while id_input != 'СТОП':
        id_input = int(id_input)
        fl = 0
        for student in reader:
            if int(student['titleProject_id']) == id_input:
                fl = 1
                student_all = student["Name"].split()
                student_cut = student_all[1][0] + '. ' + student_all[0]
                print(f'Проект № {student["titleProject_id"]} делал: {student_cut} он(а) получил(а) оценку - {student["score"]}')
                break
        if fl == 0:
            print('Ничего не найдено')
        id_input = input()
    