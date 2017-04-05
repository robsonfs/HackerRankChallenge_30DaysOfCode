from unittest import TestCase, mock
import day5

class TestDay5(TestCase):

    @mock.patch("day5.input")
    @mock.patch("day5.print")
    def test_main_call_print_ten_times(self, mock_print, mock_input):
        mock_input.return_value = "2"
        day5.main()
        times = mock_print.call_count
        self.assertEqual(10, times)

    @mock.patch("day5.input")
    @mock.patch("day5.print")
    def test_main_make_correct_print_calls(self, mock_print, mock_input):
        mock_input.return_value = "2"
        day5.main()
        mock_print.assert_any_call("2 x 1 = 2")
        mock_print.assert_any_call("2 x 2 = 4")
        mock_print.assert_any_call("2 x 3 = 6")
        mock_print.assert_any_call("2 x 4 = 8")
        mock_print.assert_any_call("2 x 5 = 10")
        mock_print.assert_any_call("2 x 6 = 12")
        mock_print.assert_any_call("2 x 7 = 14")
        mock_print.assert_any_call("2 x 8 = 16")
        mock_print.assert_any_call("2 x 9 = 18")
        mock_print.assert_any_call("2 x 10 = 20")
