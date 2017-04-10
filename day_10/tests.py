from unittest import TestCase, mock
import day10

class TestDay10(TestCase):

    def test_main_testcase0(self):
        b = day10.main(5)
        self.assertEqual(1, b)

    def test_main_testcase1(self):
        b = day10.main(13)
        self.assertEqual(2, b)

    def test_main_testcase2(self):
        b = day10.main(15)
        self.assertEqual(4, b)
