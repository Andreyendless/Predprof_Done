import csv
##=============================================================================
## Линейный поиск
'''
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    id_input = input()
    while id_input != 'СТОП':
        id_input = int(id_input)
        fl = 0
        for reader[id_found] in reader:
            if int(reader[id_found]['titleProject_id']) == id_input:
                fl = 1
                student_all = reader[id_found]["Name"].split()
                student_cut = student_all[1][0] + '. ' + student_all[0]
                print(f'Проект № {reader[id_found]["titleProject_id"]} делал: {\
                    student_cut} он(а) получил(а) оценку - {reader[id_found]["score"]}')
                break
        if fl == 0:
            print('Ничего не найдено')
        id_input = input()
'''
##=============================================================================
## Бинарный поиск
def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left+right)//2
        if value == int(arr[middle]['titleProject_id']):
            return middle
        elif value > int(arr[middle]['titleProject_id']):
            left = middle + 1
        else:
            right = middle - 1
    return -1

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for i in range(len(reader)):
        cursor = reader[i]
        cursor_score = int(cursor['score'] if cursor['score']!='None' else 0)
        pos = i
        while pos > 0 and int(reader[pos-1]['score'] if\
            reader[pos-1]['score']!='None' else 0) < cursor_score:
            reader[pos] = reader[pos-1]
            pos -= 1
        reader[pos] = cursor
    id_input = input()
    while id_input != 'СТОП':
        id_found = binary_search(reader, int(id_input))
        if id_found == -1:
            print('Ничего не найдено')
        else:
            student_all = reader[id_found]["Name"].split()
            student_cut = student_all[1][0] + '. ' + student_all[0]
            print(f'Проект № {reader[id_found]["titleProject_id"]} делал: {student_cut} он(а) получил(а) оценку - {reader[id_found]["score"]}')
        id_input = input()