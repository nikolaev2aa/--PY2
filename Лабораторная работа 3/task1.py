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
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        @property
        def duration(self) -> float:
            """Возвращает продолжительность аудиокниги."""
            return self._duration

        @duration.setter
        def duration(self, new_duration: float) -> None:
            """Устанавливает продолжительность аудиокниги."""
            if not isinstance(new_duration, float):
                raise TypeError("Продолжительность аудиокниги должна быть типа float")
            if new_duration <= 0:
                raise ValueError("Продолжительность аудиокниги должна быть положительной")
            self._duration = new_duration

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность аудиокниги: {self.duration}"


# Примеры
print(Book("Евгений Онегин", "Пушкин"))
print(PaperBook("Евгений Онегин", "Пушкин", 59))
print(AudioBook("Евгений Онегин", "Пушкин", 68.1))
