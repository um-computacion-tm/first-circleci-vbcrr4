import unittest

from main import suma, resta


class TestSuma(unittest.TestCase):
    def test_suma_positive_numbers(self):
        self.assertEqual(suma(3, 5), 8)
    
    def test_suma_negative_numbers(self):
        self.assertEqual(suma(-3, -5), -8)
    
    def test_suma_mixed_numbers(self):
        self.assertEqual(suma(3, -5), -2)
        self.assertEqual(suma(-3, 5), 2)
    
    def test_suma_zero(self):
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(3, 0), 3)
        self.assertEqual(suma(0, 5), 5)

class TestResta(unittest.TestCase):
    def test_resta_positive_numbers(self):
        self.assertEqual(resta(10, 5), 5)
    
    def test_resta_negative_numbers(self):
        self.assertEqual(resta(-10, -5), -5)
    
    def test_resta_mixed_numbers(self):
        self.assertEqual(resta(10, -5), 15)
        self.assertEqual(resta(-10, 5), -15)
    
    def test_resta_zero(self):
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(10, 0), 10)
        self.assertEqual(resta(0, 10), -10)


if __name__ == '__main__':
    unittest.main()