# Задание №1
a = 10

while True:
    user_input = int(input('Угадайте пожалуйста цифру: '))
    if a > user_input:
        print('Попробуйте снова')
    else:
        break
print('Поздравляю! Вы угадали')
