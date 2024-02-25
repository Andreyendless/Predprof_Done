import csv

def create_hash(s):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяёАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ '
    p, m = 67, 10**9+9
    hash = 0
    dictionary = {alphabet[i]: i+1 for i in range(len(alphabet))}
    power = 1
    for i in range(len(s)):
        hash += (dictionary[s[i]] * power)%m
        power = (power * p)%m
    return hash

with open('students.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))
    for student in data:
        student['id'] = create_hash(student['Name'])

with open('students_hash.csv', 'w', encoding='utf-8', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=['id','Name','titleProject_id','class','score'], delimiter=',')
    writer.writeheader()
    for student in data:
        writer.writerow(student)