import unittest
from pb02 import extra_fuel


class TestPb02Case(unittest.TestCase):
    def test_pb02(self):
        self.assertEqual(2, extra_fuel(12))
        self.assertEqual(50346, extra_fuel(100756))


if __name__ == "__main__":
    unittest.main()
