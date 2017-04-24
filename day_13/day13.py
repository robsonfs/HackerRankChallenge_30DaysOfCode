from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):

    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price

    def display(self):
        book_display = "Title: %s\nAuthor: %s\nPrice: %s"%(
            self.title, self.author, self.price
        )
        print(book_display)
        return book_display
