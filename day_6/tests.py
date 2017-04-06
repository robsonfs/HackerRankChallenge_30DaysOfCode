from unittest import TestCase, mock
import day6

class TestDay6(TestCase):

    @mock.patch("day6.print")
    @mock.patch("day6.input")
    def test_main(self, mock_input, mock_print):
        mock_input.side_effect = [2, "Hacker", "Rank"]
        day6.main()
        calls = mock_print.call_count
        mock_print.assert_any_call("Hce akr")
        mock_print.assert_any_call("Rn ak")
        self.assertEqual(2, calls)

    @mock.patch("day6.print")
    @mock.patch("day6.input")
    def test_main1(self, mock_input, mock_print):
        mock_input.side_effect = [1, "Robson"]
        day6.main()
        calls = mock_print.call_count
        mock_print.assert_any_call("Rbo osn")
        self.assertEqual(1, calls)
