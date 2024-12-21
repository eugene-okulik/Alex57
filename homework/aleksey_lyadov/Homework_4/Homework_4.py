# создание словаря и его наполнение по описанию
my_dict = {}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [1, 2, 8, False, 'hello']
my_dict['dict'] = {1: 'text', 'gdgdfgh': 456, 8: True, False: 454.6, 'hello': 'happy'}
my_dict['set'] = {'t', 2, None, False, 54645.545}

# Для того, что хранится под ключом ‘tuple’, вывожу последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’, добавляю в конец списка еще один элемент
my_dict['list'].append(None)
print(my_dict['list'])

# Удаляю второй элемент списка
my_dict['list'].pop(1)
print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’, добавляю элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict']['i am a tuple'] = 'gdgdfgergddh'
print(my_dict['dict'])

# Удаляю любой элемент
my_dict['dict'].pop(0)
print(my_dict['dict'])

# Для того, что хранится под ключом ‘set, добавляю новый элемент в множество
my_dict['set'].add('apple')
print(my_dict['set'])

# Удаляю элемент из множества
my_dict['set'].remove('t')
print(my_dict['set'])

print(my_dict)
