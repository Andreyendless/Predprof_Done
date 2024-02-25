import csv


def quick_sort(array, start, stop):
    if start >= stop: return
    left = start
    right = stop
    x = array[(left + right) // 2]
    while left <= right:
        while int(array[left]['score'] if array[left]['score']!='None' else 0) > int(x['score'] if x['score']!='None' else 0): left += 1
        while int(array[right]['score'] if array[right]['score']!='None' else 0) < int(x['score'] if x['score']!='None' else 0): right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return quick_sort(array, start, right)
    return quick_sort(array, left, stop)
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr if int(x['score'] if x['score']!='None' else 0) < int(pivot['score'] if pivot['score']!='None' else 0)]
        greater = [x for x in arr if int(x['score'] if x['score']!='None' else 0) >= int(pivot['score'] if pivot['score']!='None' else 0)]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
'''
with open('students.csv', encoding='utf-8') as file:
    base_reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    reader = quick_sort(base_reader, 0, len(base_reader)-1)
    count = 0
    print('10 класс')
    for i in range(0, len(reader), -1):
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