from unittest import TestCase, mock
from day9 import factorial
import day9

class TestDay9(TestCase):

    def test_factorial_test_case_0(self):
        n = factorial(0)
        self.assertEqual(1, n)

    def test_factorial_test_case_1(self):
        n = factorial(1)
        self.assertEqual(1, n)

    def test_factorial_test_case_2(self):
        n = factorial(2)
        self.assertEqual(2, n)

    def test_factorial_test_case_3(self):
        n = factorial(3)
        self.assertEqual(6, n)
