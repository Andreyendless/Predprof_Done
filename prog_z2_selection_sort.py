import csv
"""
def selection_sort(arr):
    for i in range(len(arr)):
        maximum = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[maximum]:
                maximum = j
        arr[maximum], arr[i] = arr[i], arr[maximum]
    return arr
"""
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for i in range(len(reader)):
        maximum = i
        for j in range(i+1, len(reader)):
            if int(reader[j]['score'] if reader[j]['score']!='None' else 0) > int(reader[maximum]['score'] if reader[maximum]['score']!='None' else 0):
                maximum = j
        reader[maximum], reader[i] = reader[i], reader[maximum]
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