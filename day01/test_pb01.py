import unittest
from pb01 import compute_fuel, compute_total_fuel


class TestPb01Case(unittest.TestCase):
    def test_compute_fuel(self):
        self.assertEqual(2, compute_fuel(12))
        self.assertEqual(2, compute_fuel(14))
        self.assertEqual(654, compute_fuel(1969))
        self.assertEqual(33583, compute_fuel(100756))

    def test_compute_total_fuel(self):
        self.assertEqual(654 + 33583, compute_total_fuel([1969, 100756]))


if __name__ == "__main__":
    unittest.main()
