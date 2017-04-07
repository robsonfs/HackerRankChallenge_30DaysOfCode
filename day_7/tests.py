from unittest import TestCase, mock
import day7

class TestDay7(TestCase):

    @mock.patch("day7.print")
    @mock.patch("day7.input")
    def test_main(self, mock_input, mock_print):
        mock_input.side_effect = ['4', '1 4 3 2']
        day7.main()
        mock_print.assert_called_with("2 3 4 1")
