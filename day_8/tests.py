from unittest import TestCase, mock
import day8

class TestDay8(TestCase):

    @mock.patch("day8.input")
    @mock.patch("day8.print")
    def test_main(self, mock_print, mock_input):
        mock_input.side_effect = [
            3, "sam 99912222", "tom 11122222", "harry 12299933",
            "sam", "alguem", "harry", ""
        ]
        day8.main()
        mock_print.assert_any_call("sam=99912222")
        mock_print.assert_any_call("Not found")
        mock_print.assert_any_call("harry=12299933")
