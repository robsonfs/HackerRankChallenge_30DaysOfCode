from unittest import TestCase, mock
from day4 import Person
import day4

class TestDay4(TestCase):

    @mock.patch("day4.print")
    def test_invalid_age(self, mock_print):
        person = Person(-5)
        mock_print.assert_called_with("Age is not valid, setting age to 0.")
        self.assertEqual(0, person.age)

    @mock.patch("day4.print")
    def test_amIOld_age_less_than_13(self, mock_print):
        person = Person(10)
        person.amIOld()
        mock_print.assert_called_with("You are young.")

    @mock.patch("day4.print")
    def test_amIOld_age_between_13_and_18(self, mock_print):
        person = Person(15)
        person.amIOld()
        mock_print.assert_called_with("You are a teenager.")

    @mock.patch("day4.print")
    def test_amIOld_greater_than_18(self, mock_print):
        person = Person(20)
        person.amIOld()
        mock_print.assert_called_with("You are old.")

    def test_yearPasses(self):
        person = Person(1)
        person.yearPasses()
        self.assertEqual(2, person.age)
