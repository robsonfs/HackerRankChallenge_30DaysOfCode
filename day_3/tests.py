from unittest import TestCase, mock
import day3

class TestDay3(TestCase):

    @mock.patch("day3.print")
    @mock.patch("day3.input")
    def test_n_is_odd(self, mock_input, mock_print):
        mock_input.return_value = "3"
        day3.main()
        mock_print.assert_any_call("Weird")

    @mock.patch("day3.print")
    @mock.patch("day3.input")
    def test_n_is_even_and_in_2_5(self, mock_input, mock_print):
        mock_input.return_value = "2"
        day3.main()
        mock_print.assert_any_call("Not Weird")
        mock_input.return_value = "4"
        day3.main()
        mock_print.assert_any_call("Not Weird")

    @mock.patch("day3.print")
    @mock.patch("day3.input")
    def test_n_is_even_and_in_6_20(self, mock_input, mock_print):
        mock_input.return_value = "12"
        day3.main()
        mock_print.assert_any_call("Weird")

    @mock.patch("day3.print")
    @mock.patch("day3.input")
    def test_n_is_even_and_in_6_20(self, mock_input, mock_print):
        mock_input.return_value = "42"
        day3.main()
        mock_print.assert_any_call("Not Weird")
