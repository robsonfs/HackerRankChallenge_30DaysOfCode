from unittest import TestCase, mock
import day2

class TestDay2(TestCase):

    @mock.patch("day2.input")
    def test_get_total_cost_of_meal(self, mock_input):
        mock_input.side_effect = [12.00, 20, 8]
        total_cost = day2.get_total_cost_of_meal()

        self.assertEqual("15", total_cost)
