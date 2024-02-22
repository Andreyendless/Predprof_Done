import csv

with open('students.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    data = list(reader)[1:]
    for id_student, name, title_project_id, class_student, score in data:
        if 'Мельников Дмитрий' in name:
            print(f'Ты получил: {score}, за проект - {title_project_id}')
            break
    class_count = {}
    class_sum = {}
    for row in data:
        class_count[row[-2]] = class_count.get(row[-2], 0) + 1
        class_sum[row[-2]] = class_sum.get(row[-2], 0) + (int(row[-1]) if row[-1] != 'None' else 0)
    for row in data:
        if row[-1] == 'None':
            row[-1] = round(class_sum[row[-2]] / class_count[row[-2]], 3)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(data)