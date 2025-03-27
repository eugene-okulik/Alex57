import mysql.connector as mysql
import dotenv
import os
import csv


dotenv.load_dotenv()


db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)


cursor = db.cursor(dictionary=True)

base_way = os.path.dirname(__file__)
homework_way = os.path.dirname(os.path.dirname(base_way))
csv_data = os.path.join(
    homework_way, 'eugene_okulik',
    'Lesson_16', 'hw_data', 'data.csv')

with open(csv_data, newline='') as data_file:
    csv_files = csv.DictReader(data_file)
    data = []
    for row in csv_files:
        data.append(row)
print(data)

data_join = cursor.execute(
    '''
    SELECT DISTINCT s.name, s.second_name, g.title AS group_title,
                b.title AS book_title, sub.title AS subject_title,
                l.title AS lesson_title, m.value AS mark_value
FROM students s
INNER JOIN books b ON b.taken_by_student_id = s.id
INNER JOIN `groups` g ON g.id = s.group_id
INNER JOIN marks m ON m.student_id = s.id
INNER JOIN lessons l ON l.id = m.lesson_id
INNER JOIN subjets sub ON sub.id = l.subject_id
    '''
)
print_join = cursor.fetchall()
print(print_join)

missing_in_join = []

for item in data:
    if item not in print_join:
        missing_in_join.append(item)

if missing_in_join:
    print("В print_join отсутствуют:")
    for item in missing_in_join:
        print(item)
else:
    print("Все данные из data есть в print_join")
