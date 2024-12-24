# Задание №1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание №2
a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
index_a = a.index('42')
index_b = b.index('514')
index_c = c.index('9')
int_a = int(a[index_a:])
int_b = int(b[index_b:])
int_c = int(c[index_c:])
print(int_a + 10, int_b + 10, int_c + 10)

# Задание №2
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print(f'Students {students} study these subjects: {subjects}')
