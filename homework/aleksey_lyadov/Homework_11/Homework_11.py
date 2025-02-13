# Первый класс Book


class Book:
    page_material = 'бумага'
    presence_text = True

    def __init__(self, book_name, author, number_pages, isbn, reserved=False):
        self.book_name = book_name
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        reserved_status = (f"Название: {self.book_name}, "
                           f"Автор: {self.author}, страниц: "
                           f"{self.number_pages}, "
                           f"материал: {self.page_material}")
        if self.reserved:
            reserved_status += ', зарезервирована'
        return reserved_status


class Textbooks(Book):
    tasks = True

    def __str__(self):
        objects = 'Математика'
        class_school = 9
        print_names = (f"Название: {self.book_name}, Автор: {self.author}, "
                       f"предмет: {objects}, класс: {class_school}")
        if self.reserved:
            print_names += ', зарезервирована'
        return print_names


book_Idiot = Book('Идиот', 'Достоевский', 500, 34, True)
print(book_Idiot)
book_quiet_qon = Book('Тихий Дон', 'Шолохов', 300, 24, False)
print(book_quiet_qon)
dollhouse = Book('Кукольный дом', 'Генрик Ибсен', 400, 134, True)
print(dollhouse)
war_and_peace = Book('Война и мир', 'Лев Толстой', 1300, 124, False)
print(war_and_peace)
moby_dick = Book('Моби Дик', 'Герман Мелвилл', 360, 155, False)
print(moby_dick)
algebra_book1 = Textbooks('Алгебра', 'Иванов', 200, 1334, True)
print(algebra_book1)
algebra_book2 = Textbooks('Алгебра', 'Иванов', 200, 2234, False)
print(algebra_book2)
