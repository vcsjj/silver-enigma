from unittest import TestCase

from Indicators.EmaIndicator import EmaIndicator


class TestEmaIndicator(TestCase):
    def test_calculate_with_alpha(self):
        alpha = 0.5
        y = [0, 10, 100]
        result = EmaIndicator().calculate_with_alpha(y, alpha)
        self.assertEqual(y[0], result[0])
        self.assertEqual(alpha * y[1] + (1 - alpha) * result[0], result[1])
        self.assertEqual(alpha * y[2] + (1 - alpha) * result[1], result[2])
