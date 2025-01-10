# Задание №1
texts = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

format_text = texts.split()
fin_text = []
for text in format_text:
    if text[-1] in [',', '.']:
        fin_text.append(text[:-1] + 'ing' + text[-1])
    else:
        fin_text.append(text + 'ing')
join_text = ' '.join(fin_text)
print(join_text)


