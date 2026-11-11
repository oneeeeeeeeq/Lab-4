import unittest
from square import square_area, square_perimeter

class SquareTestCase(unittest.TestCase):
    """Тесты для вычислений параметров квадрата."""

    def test_area_zero(self):
        """Тестирует площадь квадрата с нулевой стороной."""
        self.assertEqual(square_area(0), 0)

    def test_area_integer(self):
        """Тестирует площадь квадрата с целой стороной."""
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(10), 100)

    def test_area_float(self):
        """Тестирует площадь квадрата с дробной стороной."""
        self.assertEqual(square_area(1.5), 2.25)

    def test_perimeter_zero(self):
        """Тестирует периметр квадрата с нулевой стороной."""
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_integer(self):
        """Тестирует периметр квадрата с целой стороной."""
        self.assertEqual(square_perimeter(3), 12)

    def test_perimeter_float(self):
        """Тестирует периметр квадрата с дробной стороной."""
        self.assertEqual(square_perimeter(2.5), 10.0)