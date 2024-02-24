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
        for reader[middle] in reader:
            if int(reader[middle]['titleProject_id']) == id_input:
                fl = 1
                student_all = reader[middle]["Name"].split()
                student_cut = student_all[1][0] + '. ' + student_all[0]
                print(f'Проект № {reader[middle]["titleProject_id"]} делал: {\
                    student_cut} он(а) получил(а) оценку - {reader[middle]["score"]}')
                break
        if fl == 0:
            print('Ничего не найдено')
        id_input = input()
'''
##=============================================================================
## Бинарный поиск
'''
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
'''
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    reader = sorted(reader, key=lambda x: int(x['titleProject_id']))
    id_input = input()
    while id_input != 'СТОП':
        id_input = int(id_input)
        left, right = 0, len(reader)-1
        while left <= right:
            middle = (left+right)//2
            if id_input == int(reader[middle]['titleProject_id']):
                student_all = reader[middle]["Name"].split()
                student_cut = student_all[1][0] + '. ' + student_all[0]
                print(f'Проект № {reader[middle]["titleProject_id"]} делал: {student_cut} он(а) получил(а) оценку - {reader[middle]["score"]}')
                break
            elif id_input > int(reader[middle]['titleProject_id']):
                left = middle + 1
            else:
                right = middle - 1
        else:
            print('Ничего не найдено')
        id_input = input()