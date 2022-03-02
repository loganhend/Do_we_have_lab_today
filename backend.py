class Book:
    def __init__(self, book_name, author_name, publisher, parts, edition):
        self.__book_name = book_name
        self.__author_name = author_name
        self.__publisher = publisher
        self.__parts = parts
        self.__edition = edition
        self.__total_parts = parts * edition

    def get_bookname(self):
        return self.__book_name

    def get_authorname(self):
        return self.__author_name

    def get_publisher(self):
        return self.__publisher

    def get_parts(self):
        return self.__parts

    def get_total_parts(self):
        return self.__total_parts

    def get_edition(self):
        return self.__edition


class List:
    # конструктор??
    __books = []
    __curr_notes_per_page = 10
    __curr_page = 1

    def next_page(self):
        if self.__curr_page != len(self.__books)/self.__curr_notes_per_page:
            self.__curr_page += 1
            # перерисовывается окно

    def prev_page(self):
        if self.__curr_page != 1:
            self.__curr_page -= 1
            # перерисовывается окно

    def last_page(self):
        if self.__curr_page != len(self.__books) / self.__curr_notes_per_page:
            self.__curr_page = len(self.__books) / self.__curr_notes_per_page
            # перерисовывается окно

    def first_page(self):
        if self.__curr_page != 1:
            self.__curr_page = 1
            # перерисовывается окно

    def change_per_page(self, per_page):
        num = self.__curr_notes_per_page * self.__curr_page + 1
        self.__curr_notes_per_page = per_page
        self.__curr_page = num // self.__curr_notes_per_page + 1
        # перерисовывается окно


class MainList(List):
    def __init__(self):
        self.__curr_notes_per_page = 10
        self.__curr_page = 1

    def search(self):
        pass


class ResultList(List):
    def __init__(self, books):
        self.__books = books
