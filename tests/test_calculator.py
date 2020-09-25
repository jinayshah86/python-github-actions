import unittest

from pgb import add, mul, pow, sub


class TestCalculator(unittest.TestCase):
    def test_add(self):
        a = 5
        b = 10
        self.assertEqual(add.add(a, b), 15)

    def test_mul(self):
        a = 5
        b = 10
        self.assertEqual(mul.mul(a, b), 50)

    def test_sub(self):
        a = 5
        b = 10
        self.assertEqual(sub.sub(a, b), -5)

    def test_pow(self):
        a = 2
        b = 10
        self.assertEqual(pow.pow(a, b), 1024)


if __name__ == "__main__":
    unittest.main()
