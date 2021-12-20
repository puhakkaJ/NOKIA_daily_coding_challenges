import unittest
from sport import Athlete


class TestClass(unittest.TestCase):
    def test_age(self):
        athlete = Athlete("Jenni", 22, 175, 60)
        result = athlete.get_age()
        self.assertEqual(result, "Jenni is age 22")

    def test_height(self):
        athlete = Athlete("Pekka", 67, 160, 40)
        result = athlete.get_height()
        self.assertEqual(result, "Pekka is 160cm")

    def test_weight(self):
        athlete = Athlete("Nenna", 6, 90, 34)
        result = athlete.get_weight()
        self.assertEqual(result, "Nenna weights 34kg")


if __name__ == '__main__':
    unittest.main()