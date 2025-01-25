# Задание №3
a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'

a_int = int(a.split(': ')[1])
b_int = int(b.split(': ')[1])
c_int = int(c.split(': ')[1])
d_int = int(d.split(': ')[1])


def fin_summ(*args):
    result = 10
    return ' '.join(str(summ + result) for summ in args)


print(fin_summ(a_int, b_int, c_int, d_int))

# Более правильный код будет выглядеть так,
# тут избавляемся от повторений переменных со split с помощью цикла
str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'


def finn_summ(*args):
    nums = []
    for num in args:
        nums.append(int(num.split(': ')[1]))
    add_num = 10
    return ' '.join(str(x + add_num) for x in nums)


print(fin_summ(str1, str2, str3, str4))
