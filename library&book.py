class book:
    def __init__(self, title, author, available=True):
        self.title = str(title)
        self.author = str(author)
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False

    def return_book(self):
        if not self.available:
            self.available = True


class library:
    def __init__(self, books=[]):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        if len(self.books) > 0:
            for i in self.books:
                if i.title == title and i.available:
                    i.borrow()
                    return f'{title} has been borrowed'
            return f'{title} is not available for borrowing'

    def return_book(self, title):
        if len(self.books) > 0:
            for i in self.books:
                if i.title == title and not i.available:
                    i.return_book()
                    return f'{title} has been returned'
            return f'{title} is returned befor '

    def show_available_book(self):
        if len(self.books) > 0:
            av_books = []
            for i in self.books:
                if i.available == True:
                    av_books.append(i.title)
            return av_books
