import unittest
from pgb import add, mul


class TestCalculator(unittest.TestCase):
    def test_add(self):
        a = 5
        b = 10
        self.assertEqual(add.add(a, b), 15)

    def test_mul(self):
        a = 5
        b = 10
        self.assertEqual(mul.mul(a, b), 50)


if __name__ == '__main__':
    unittest.main()
