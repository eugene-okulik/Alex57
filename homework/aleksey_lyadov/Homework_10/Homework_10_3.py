# Задание №3.1


first_int = int(input('Назовите первое число: '))
second_int = int(input('Назовите второе число: '))


def func_calc(func):

    def wrapper(first, second):
        if first == second:
            operation = first + second
            print(operation)
        elif first > second:
            operation = second - first
            print(operation)
        elif first < second:
            operation = first / second
            print(operation)
        elif first < 0 and second < 0:
            operation = first * second
            print(operation)
        return func(first, second, operation)
    return wrapper


@func_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second


calc(first_int, second_int)
