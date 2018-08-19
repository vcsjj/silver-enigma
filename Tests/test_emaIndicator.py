from unittest import TestCase

from Indicators.EmaIndicator import EmaIndicator


class TestEmaIndicator(TestCase):
    def test_evenly_spaced(self):
        alpha = 0.5
        s = [0, 10, 100]
        result = EmaIndicator().calculate_with_alpha(s, alpha)
        self.assertEqual(s[0], result[0])
        self.assertEqual(s[1], result[1])
        self.assertEqual(s[2], result[2] + 0.5 * result[1])
