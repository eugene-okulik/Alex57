import os
import argparse


def setup_argparse():
    """Настройка парсера аргументов командной строки"""
    parser = argparse.ArgumentParser(
        description='Анализатор лог-файлов: поиск текста с контекстом',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'path',
        help='Путь к папке с лог-файлами')
    parser.add_argument(
        '--text', '-t',
        required=True,
        help='Текст для поиска (регистр не учитывается)')
    parser.add_argument(
        '--context', '-c',
        type=int,
        default=5,
        help='Количество слов контекста с каждой стороны')

    return parser.parse_args()


def find_text_in_files(folder_path, search_text, context_size):
    """Основная функция поиска текста в файлах"""

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                process_file(file, filename, search_text, context_size)
        except IOError as e:
            print(f"\nОшибка чтения файла {filename}: {e}")
        except Exception as e:
            print(f"\nОшибка обработки файла {filename}: {e}")


def process_file(file, filename, search_text, context_size):
    """Обрабатывает один файл"""
    search_lower = search_text.lower()

    for line_num, line in enumerate(file, 1):
        words = line.split()
        for i, word in enumerate(words):
            if search_lower in word.lower():
                start_idx = max(0, i - context_size)
                end_idx = min(len(words), i + context_size + 1)
                context = ' '.join(words[start_idx:end_idx])
                print(f"\nФайл: {filename}, Строка {line_num}")
                print(f"Контекст: ...{context}...")


if __name__ == "__main__":
    args = setup_argparse()

    if not os.path.isdir(args.path):
        print(f"Ошибка: {args.path} не является папкой!")
        exit(1)

    find_text_in_files(args.path, args.text, args.context)
