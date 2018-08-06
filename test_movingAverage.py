from unittest import TestCase

from MovingAverage import MovingAverage


class TestMovingAverage(TestCase):
    def test_MovingAverageHasLessElements(self):
        values = [1, 2, 3]
        ma = MovingAverage().EvenlySpaced(values, 2)
        self.assertEqual(len(values), len(ma) + 1)

    def test_MovingAverageComputesCorrectlyForLength2(self):
        l = [0, 2, 0]
        expected = [1, 1]
        result = MovingAverage().EvenlySpaced(l, 2)
        self.assertListEqual(expected, result)

    def test_MovingAverageComputesCorrectlyForLength1(self):
        l = [0, 2, 0]
        expected = [0, 2, 0]
        result = MovingAverage().EvenlySpaced(l, 1)
        self.assertListEqual(expected, result)

    def test_MovingAverageComputesCorrectlyForLength3(self):
        l = [0, 2, 0]
        expected = [2 / 3]
        result = MovingAverage().EvenlySpaced(l, 3)
        self.assertListEqual(expected, result)

    def test_MovingDateAverageWith1DayEvenSpacing(self):
        d = {1: 1, 2: 4, 3: 5}
        expected = {2: 5 / 2, 3: 9 / 2}
        result = MovingAverage().ArbitrarySpacing(d, 2)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpacing(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {3: 5 / 2, 5: 9 / 2}
        result = MovingAverage().ArbitrarySpacing(d, 2)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpacingLength3(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {3: (1+1+4) / 3, 5: (4+4+5) / 3}
        result = MovingAverage().ArbitrarySpacing(d, 3)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpacingLength4(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {5: (1+4+4+5) / 4}
        result = MovingAverage().ArbitrarySpacing(d, 3)
        self.assertEqual(expected, result)
