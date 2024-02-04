class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        :param id_: Идентификатор книги (целое число)
        :param name: Название книги (строка)
        :param pages: Количество страниц в книге (целое число)
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self) -> str:
        """
        Возвращает строку, которая может быть использована для инициализации экземпляра класса.

        :return: Строка для инициализации экземпляра класса
        """
        return f'Book(id_={self.id}, name="{self.name}", pages={self.pages})'


class Library:
    def __init__(self, books: list = None):
        """
        Конструктор класса Library.

        :param books: Список книг (список экземпляров класса Book)
        """
        self.books = books or []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор для новой книги
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке.

        :param book_id: Идентификатор книги (целое число)
        :return: Индекс книги в списке
        :raises ValueError: Если книги с запрашиваемым id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id={book_id} не существует")


if __name__ == '__main__':
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
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
