from unittest import TestCase, mock
from day14 import Difference

class TestDay14(TestCase):

    def setUp(self):
        self.d = Difference([1, 2, 5])

    def test_difference_has_maximumDifference_att(self):
        self.assertTrue(hasattr(self.d, 'maximumDifference'))

    def test_computeDifference(self):
        difference = self.d.computeDifference()
        self.assertEqual(4, difference)

    def test_computeDifference_alter_maximumDifference_attr(self):
        difference = self.d.computeDifference()
        self.assertTrue(0 < self.d.maximumDifference)
