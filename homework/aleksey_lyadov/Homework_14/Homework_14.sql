-- Создайте студента (student)
-- тут я не смог сначала создать студента с group_id из-за конфликта и выставил Null т.к. был конфликт
INSERT INTO students (name, second_name, group_id) VALUES ('Alexey', 'Homework', Null)
-- Далее чтобы подтянуть group_id я в 3-ем шаге создал группу с id 3069 и дообновил своего студента
UPDATE students SET group_id = 3069 WHERE id = 4760


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('Python test book', 4760)
INSERT INTO books (title, taken_by_student_id) VALUES ('Auto test book2', 4760)
INSERT INTO books (title, taken_by_student_id) VALUES ('Auto tt book2', 4760)



-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Homework14 group', 'март 2025', 'декабрь 2025')


-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Python test course')
INSERT INTO subjets (title) VALUES ('SQLtest course')


--Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 14 python', 4950)
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 14 sql', 4951)


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 8990, 4760)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 8989, 4760)


-- Получите информацию из базы данных:

-- Все оценки студента
SELECT marks.value FROM marks WHERE student_id = 4760


-- Все книги, которые находятся у студента
SELECT books.title FROM books WHERE taken_by_student_id = 4760


-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
-- оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
SELECT DISTINCT s.name, s.second_name, g.title AS 'Название группы',
                b.title AS 'Название книги', m.value, l.title AS 'Занятие',
                sub.title AS 'Предмет'
FROM students s
INNER JOIN books b ON b.taken_by_student_id = s.id
INNER JOIN `groups` g ON g.id = s.group_id
INNER JOIN marks m ON m.student_id = s.id
INNER JOIN lessons l ON l.id = m.lesson_id
INNER JOIN subjets sub ON sub.id = l.subject_id
WHERE s.id = 4760;
