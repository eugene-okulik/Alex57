# Задание №3.2


prise_list = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

prise_split = prise_list.split()
list_dict = dict(zip(prise_split[::2], map(lambda x:
                                           int(x.replace('р', '')), (prise_split[1::2]))))
print(list_dict)
