import os
import re


def find_text_in_files():
    while True:
        folder_path = input('Укажите полный путь к папке с логами: ').strip()
        search_text = input('Введите текст для поиска: ').strip()
        break
    # поиск без учёта регистра
    search_pattern = re.compile(re.escape(search_text), re.IGNORECASE)

    # поиск всех файлов в переданной директории
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r') as file:
                # перебирает строки файла, нумеруя их начиная с 1
                for line_num, line in enumerate(file, 1):
                    matches = list(search_pattern.finditer(line))
                    if not matches:
                        continue

                    # Разбиваем строку на слова с сохранением позиций
                    words = []
                    for m in re.finditer(r'\b(\w+)\b', line):  # Ищем только слова
                        words.append((m.start(), m.end(), m.group()))

                    for match in matches:
                        start_pos, end_pos = match.start(), match.end()

                        # Находим индекс слова, содержащего совпадение
                        match_word_idx = next(
                            (i for i, (w_start, w_end, _) in enumerate(words)
                             if w_start <= start_pos < w_end),-1)

                        if match_word_idx == -1:
                            continue

                        # Определяем диапазон слов для контекста
                        start_idx = max(0, match_word_idx - 5)
                        end_idx = min(len(words), match_word_idx + 6)  # +1 для включения 5 слов после

                        # Собираем контекст с сохранением оригинальных пробелов между словами
                        context_parts = [words[start_idx][2]]  # Начинаем с первого слова

                        # Добавляем остальные слова с пробелами между ними
                        for i in range(start_idx + 1, end_idx):
                            prev_end = words[i - 1][1]
                            curr_start = words[i][0]
                            context_parts.append(line[prev_end:curr_start])  # Пробелы между словами
                            context_parts.append(words[i][2])  # Само слово

                        context = ''.join(context_parts).strip()

                        print(f"\nФайл: {filename}, Строка {line_num}")
                        print(f"Контекст: ...{context}...")

        except IOError as e:
            print(f"\nОшибка чтения файла {filename}: {e}")
        except Exception as e:
            print(f"\nОшибка обработки файла {filename}: {e}")


find_text_in_files()