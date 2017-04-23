from unittest import TestCase, mock
import day11

class TestDay11(TestCase):

    def setUp(self):
        self.arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]

    def test_get_hourglasses(self):
        hourglasses = day11.get_hourglasses(self.arr)

        self.assertEqual(16, len(hourglasses))

    def test_get_max_sum(self):
        hourglasses = day11.get_hourglasses(self.arr)
        max_sum = day11.get_max_sum(hourglasses)
        self.assertEqual(19, max_sum)
