# Задание №1
import datetime
import statistics


date_time = "Jan 15, 2023 - 12:05:33"
python_date_time = datetime.datetime.strptime(date_time,
                                              "Jan %d, %Y - %H:%M:%S")
print(python_date_time.strftime("%B"))
print(python_date_time.strftime("%d.%m.%Y, %H:%M"))

# Задание №2
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
temperatures_now = list(filter(lambda x: x > 28, temperatures))
print(max(temperatures_now))
print(min(temperatures_now))
print(int(statistics.mean(temperatures_now)))
