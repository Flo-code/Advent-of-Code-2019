import unittest
from pb01 import count_password


class TestPb01Case(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(1, count_password(111111, 111111))
        self.assertEqual(0, count_password(223450, 223450))
        self.assertEqual(0, count_password(123789, 123789))


if __name__ == "__main__":
    unittest.main()
