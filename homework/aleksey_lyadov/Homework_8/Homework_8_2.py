# Задание №2
# Тут результат на стотысячном шаге падает с ошибкой,
# что не хватает памяти, так задумано или нет?
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


count = 1
for number in fib():
    if count == 5 or count == 200 or count == 1000 or count == 100000:
        print(number)
    if count == 100000:
        break
    count += 1
