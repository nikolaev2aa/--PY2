class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property   # атрибут только для чтения (read-only)
    def name(self):
        return self._name

    @property   # атрибут только для чтения (read-only)
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int) and pages > 0:  # Проверка на корректность входных данных
            self.pages = pages
        else:
            raise AttributeError(f'Некорректное количество страниц:{pages!r}')

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float) and duration > 0:  # Проверка на корректность входных данных
            self.duration = duration
        else:
            raise AttributeError(f'Некорректная продолжительность аудиокниги:{duration!r}')

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность аудиокниги: {self.duration}"


# Примеры
print(Book("Евгений Онегин", "Пушкин"))
print(PaperBook("Евгений Онегин", "Пушкин", 59))
print(AudioBook("Евгений Онегин", "Пушкин", 68.1))
