import unittest
from triangle import triangle_area, triangle_perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для вычислений параметров треугольника."""

    def test_area_zero(self):
        """Тестирует площадь треугольника с нулевым основанием или высотой."""
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)

    def test_area_integer(self):
        """Тестирует площадь треугольника с целыми значениями."""
        self.assertEqual(triangle_area(4, 6), 12.0)

    def test_area_float(self):
        """Тестирует площадь треугольника с дробными значениями."""
        self.assertEqual(triangle_area(3.5, 2.0), 3.5)

    def test_perimeter_integer(self):
        """Тестирует периметр треугольника с целыми сторонами."""
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        """Тестирует периметр треугольника с дробными сторонами."""
        self.assertEqual(triangle_perimeter(1.1, 2.2, 3.3), 6.6)