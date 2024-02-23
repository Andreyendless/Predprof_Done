import csv
"""
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        all_sorted = True
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                all_sorted = False
                arr[j+1], arr[j] = arr[j], arr[j+1]
        if all_sorted:
            return arr
"""
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for i in range(0, len(reader)-1):
        all_sorted = True
        for j in range(0, len(reader)-i-1):
            if int(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < int(reader[j+1]['score'] if reader[j+1]['score'] != 'None' else 0):
                all_sorted = False
                reader[j+1], reader[j] = reader[j], reader[j+1]
        if all_sorted:
            break
    count = 0
    print('10 класс')
    for i in range(len(reader)):
        if '10' in reader[i]['class'] and count < 3:
            count += 1
            student_all = reader[i]["Name"].split()
            student_cut = student_all[1][0] + '. ' + student_all[0]
            print(f'{count} место: {student_cut}')