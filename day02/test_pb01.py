import unittest
from pb01 import assist_program


class TestPb01Case(unittest.TestCase):
    def test_pb01(self):
        self.assertEqual(
            3500, assist_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        )


if __name__ == "__main__":
    unittest.main()
