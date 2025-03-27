import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)


# Создайте студента (student)
query_students = \
    'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
value_students = ('Alexey', 'Homework', None)
cursor.execute(query_students, value_students)
id_students = cursor.lastrowid
print(f"Создан студент с ID: {id_students}")

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
value_books = [
    ('Python test book', id_students),
    ('Auto test book2', id_students),
    ('Auto tt book2', id_students)
]
cursor.executemany(query_books, value_books)
print("Добавлены книги для студента")

# Создайте группу (group) и определите своего студента туда
query_groups = \
    'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
value_groups = ('Homework14 group', 'март 2025', 'декабрь 2025')
cursor.execute(query_groups, value_groups)
id_groups = cursor.lastrowid
print(f"Создана группа с ID: {id_groups}")

# Обновите своего студента
update_student = \
    'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(
    update_student, (id_groups, id_students))
print("Студент обновлен с указанием группы")

# Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO subjets (title) VALUES ('Python test course')")
id_subjets1 = cursor.lastrowid
print(f"Создан предмет 'Python test course' с ID: {id_subjets1}")

cursor.execute("INSERT INTO subjets (title) VALUES ('SQLtest course')")
id_subjets2 = cursor.lastrowid
print(f"Создан предмет 'SQLtest course' с ID: {id_subjets2}")

# Создайте по два занятия для каждого предмета (lessons)
add_lessons1 = (
    "INSERT INTO lessons (title, subject_id) "
    "VALUES ('Lesson 14 python', %s)")
cursor.execute(add_lessons1, (id_subjets1,))
id_lessons1 = cursor.lastrowid
print(f"Создано занятие 'Lesson 14 python' с ID: {id_lessons1}")

add_lessons2 = (
    "INSERT INTO lessons (title, subject_id) "
    "VALUES ('Lesson 14 sql', %s)")
cursor.execute(add_lessons2, (id_subjets2,))
id_lessons2 = cursor.lastrowid
print(f"Создано занятие 'Lesson 14 sql' с ID: {id_lessons2}")

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query_marks = \
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
value_marks = [
    (5, id_lessons1, id_students),
    (4, id_lessons2, id_students)
]
cursor.executemany(query_marks, value_marks)
print("Добавлены оценки для студента")

# Получите информацию из базы данных:
# Все оценки студента
select_marks = (
    'SELECT marks.value FROM marks '
    'WHERE student_id = %s')
cursor.execute(select_marks, (id_students,))
marks = cursor.fetchall()
print("\nОценки студента:")
for mark in marks:
    print(f"Оценка: {mark['value']}")

# Все книги, которые находятся у студента
select_books = (
    'SELECT books.title FROM books '
    'WHERE taken_by_student_id = %s')
cursor.execute(select_books, (id_students,))
books = cursor.fetchall()
print("\nКниги студента:")
for book in books:
    print(f"Книга: {book['title']}")

# Для вашего студента выведите всё,
# что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
join_students = '''
SELECT DISTINCT s.name, s.second_name, g.title AS group_title,
                b.title AS book_title, m.value, l.title AS lesson_title,
                sub.title AS subject_title
FROM students s
INNER JOIN books b ON b.taken_by_student_id = s.id
INNER JOIN `groups` g ON g.id = s.group_id
INNER JOIN marks m ON m.student_id = s.id
INNER JOIN lessons l ON l.id = m.lesson_id
INNER JOIN subjets sub ON sub.id = l.subject_id
WHERE s.id = %s;
'''
cursor.execute(join_students, (id_students,))
student_info = cursor.fetchall()
print("\nПолная информация о студенте:")
for info in student_info:
    print(f"Имя: {info['name']}, Фамилия: {info['second_name']}")
    print(f"Группа: {info['group_title']}")
    print(f"Книга: {info['book_title']}")
    print(
        f"Оценка: {info['value']}, Занятие: "
        f"{info['lesson_title']}, Предмет: {info['subject_title']}")
    print("-" * 40)
db.commit()


db.close()
