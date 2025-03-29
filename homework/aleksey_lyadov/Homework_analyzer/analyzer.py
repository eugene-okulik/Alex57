import os


while True:
    user_directory = input('Укажите полный путь к папке, в которой лежат файлы с логами: ')
    user_text = input('Укажите какой текст нужно найти в файлах: ')
    break

with open(user_directory, 'r') as log_file:
    for line in log_file.readlines():
        print(line)
