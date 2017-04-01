from unittest import TestCase, mock
import day0

class TestDay0(TestCase):

    @mock.patch("day0.input")
    @mock.patch("day0.print")
    def test_print_hello_world(self, mock_print, mock_input):
        day0.main()
        mock_print.assert_any_call("Hello, World.")

    @mock.patch("day0.print")
    @mock.patch("day0.input")
    def test_print_input_string(self, mock_input, mock_print):
        mock_input.return_value = "Anything"
        day0.main()
        mock_print.assert_any_call("Anything")
