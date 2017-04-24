from unittest import TestCase, mock
from day13 import Book, MyBook
import day13

class TestDay13(TestCase):

    def setUp(self):
        self.book = MyBook(
            "Padrões de Projeto em Python", "Robson Fernandes", 29.90
        )

    def test_my_book_is_a_book_subclass(self):
        self.assertTrue(issubclass(MyBook, Book))

    @mock.patch("day13.print")
    def test_diplay_calls_print(self, mock_print):
        self.book.display()
        mock_print.assert_called_with(
            "Title: Padrões de Projeto em Python\nAuthor: Robson Fernandes\nPrice: 29.9"
        )
