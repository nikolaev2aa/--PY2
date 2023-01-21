BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):  # Инициализация атрибутов
        self.id = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book] = None):  # Инициализация списка книг
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):  # Метод, возвращающий идентификатор для добавления новой книги в библиотеку
        if len(self.books) == 0:  # Проверка на наличие книг в исходной библиотеке
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_):  #Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса
        if not self.books:  #Случай пустой библиотеки
            raise ValueError("Книги с таким ID не существует")
        else:
            for index, self.books[index] in enumerate(self.books):
                if self.books[index].id == id_:  # Проверка соответствия
                    return index  # Индекс книги из списка
                return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
