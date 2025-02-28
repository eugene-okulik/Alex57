import os
from datetime import datetime, timedelta


base_way = os.path.dirname(__file__)
homework_way = os.path.dirname(os.path.dirname(base_way))
eugene_okulik_way = os.path.join(
    homework_way, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_okulik_way)


def read_file():

    with open(eugene_okulik_way, 'r') as data_file:
        for line in data_file.readlines():
            # Убираем лишние пробелы и символы переноса строки
            yield line.strip()


# Функция для обработки даты и времени
def process_date(line):
    datetime_str = " ".join(line.split()[1:3])

    # Преобразуем строку в объект datetime
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
    return dt


for date_line in read_file():
    dt = process_date(date_line)

    # Распечатываем дату на неделю позже
    if '2023-11-27' in date_line:
        new_date = dt + timedelta(weeks=1)
        print(f"Дата на неделю позже: {new_date}")

    # Распечатываем день недели
    if '2023-07-15' in date_line:
        day_week = dt.strftime('%A')
        print(f'День недели для 2023-07-15: {day_week}')

    # Распечатываем сколько дней назад была эта дата
    if '2023-06-12' in date_line:
        days_ago = (datetime.now() - dt).days
        print(f"Дней назад с 2023-06-12: {days_ago}")
