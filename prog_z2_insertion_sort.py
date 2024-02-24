import csv
'''
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr
'''
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    ##print(*reader, sep='\n')
    for i in range(len(reader)):
        cursor = reader[i]
        cursor_score = int(cursor['score'] if cursor['score']!='None' else 0)
        pos = i
        while pos > 0 and int(reader[pos-1]['score'] if reader[pos-1]['score']!='None' else 0)\
                < cursor_score:
            reader[pos] = reader[pos-1]
            pos -= 1
        reader[pos] = cursor
    count = 0
    print('10 класс')
    for i in range(len(reader)):
        if '10' in reader[i]['class'] and count < 3:
            count += 1

            student_all = reader[i]["Name"].split()
            student_cut = student_all[1][0] + '. ' + student_all[0]
            print(f'{count} место: {student_cut}')
"""Вывод:
10 класс
1 место: Д. Дориков
2 место: В. Королупов
3 место: И. Моторыгин
"""