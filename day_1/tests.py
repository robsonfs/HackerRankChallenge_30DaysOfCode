from unittest import TestCase, mock
import day1

class TestDay1(TestCase):

    @mock.patch("day1.input")
    @mock.patch("day1.print")
    def test_print_sum_of_integers(self, mock_print, mock_input):
        mock_input.side_effect = [
            42,
            42.0,
            "is the best place to learn and practice coding!."
        ]
        day1.main()
        mock_print.assert_any_call("46")

    @mock.patch("day1.input")
    @mock.patch("day1.print")
    def test_print_sum_of_floats(self, mock_print, mock_input):
        mock_input.side_effect = [
            42,
            42.0,
            "is the best place to learn and practice coding!."
        ]
        day1.main()
        mock_print.assert_any_call("46.0")

    @mock.patch("day1.input")
    @mock.patch("day1.print")
    def test_print_string_concatenation(self, mock_print, mock_input):
        mock_input.side_effect = [
            42,
            42.0,
            "is the best place to learn and practice coding!."
        ]
        day1.main()
        mock_print.assert_any_call("HackerRank is the best place to learn and practice coding!.")
