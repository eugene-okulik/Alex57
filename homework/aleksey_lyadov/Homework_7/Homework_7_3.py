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
