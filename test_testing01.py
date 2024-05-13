import unittest
from testing01 import area
from math import pi

class TestArea(unittest.TestCase):
    def test_area(self):
        print("--Test valores resultado conocido")
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(3), pi*(3**2))
        