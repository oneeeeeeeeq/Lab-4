import unittest
from rectangle import rectangle_area, rectangle_perimeter

class RectangleTestCase(unittest.TestCase):
    """Тесты для вычислений параметров прямоугольника."""

    def test_area_zero(self):
        """Тестирует площадь прямоугольника, если одна из сторон равна нулю."""
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(10, 0), 0)

    def test_area_integer(self):
        """Тестирует площадь прямоугольника с целыми сторонами."""
        self.assertEqual(rectangle_area(2, 3), 6)

    def test_area_float(self):
        """Тестирует площадь прямоугольника с дробными сторонами."""
        self.assertEqual(rectangle_area(1.5, 2.0), 3.0)

    def test_perimeter_zero(self):
        """Тестирует периметр прямоугольника с нулевыми сторонами."""
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_perimeter_integer(self):
        """Тестирует периметр прямоугольника с целыми сторонами."""
        # Формула из файла: 2 * (a + b)
        self.assertEqual(rectangle_perimeter(2, 3), 10)

    def test_perimeter_float(self):
        """Тестирует периметр прямоугольника с дробными сторонами."""
        self.assertEqual(rectangle_perimeter(1.5, 2.5), 8.0)