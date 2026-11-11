import unittest
import math
from circle import circle_area, circle_perimeter

class CircleTestCase(unittest.TestCase):
    """Тесты для вычислений параметров круга."""

    def test_area_zero(self):
        """Тестирует площадь круга с нулевым радиусом."""
        self.assertEqual(circle_area(0), 0)

    def test_area_integer(self):
        """Тестирует площадь круга с целым радиусом."""
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(5), 25 * math.pi)

    def test_area_float(self):
        """Тестирует площадь круга с дробным радиусом."""
        self.assertAlmostEqual(circle_area(2.5), 6.25 * math.pi)

    def test_perimeter_zero(self):
        """Тестирует длину окружности с нулевым радиусом."""
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_integer(self):
        """Тестирует длину окружности с целым радиусом."""
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)

    def test_perimeter_float(self):
        """Тестирует длину окружности с дробным радиусом."""
        self.assertAlmostEqual(circle_perimeter(3.5), 7 * math.pi)