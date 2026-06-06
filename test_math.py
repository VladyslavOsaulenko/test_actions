import unittest
from math_operations import add_numbers

class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Перевіряємо, чи 2 + 3 дійсно дорівнює 5
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        # Перевіряємо роботу з від'ємними числами
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()