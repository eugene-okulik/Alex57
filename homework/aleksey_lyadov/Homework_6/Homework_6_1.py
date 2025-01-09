# Задание №1
texts = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
         'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

format_text = texts.split()
for text in format_text:
    text_ing = 'ing' + text
    print(text_ing, end=" ")
