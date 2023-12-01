import unittest
from first import averageValue


class TestAverageValue(unittest.TestCase):

    def test_avg(self):
        self.assertEqual(averageValue([1,1,11,1,1,1,1]), averageValue([1,2,11,4,1,564,1]))