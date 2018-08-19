from unittest import TestCase

from MovingAverage import MovingAverage


class TestMovingAverage(TestCase):
    def test_MovingAverageHasLessElements(self):
        values = [1, 2, 3]
        ma = MovingAverage().evenly_spaced(values, 2)
        self.assertEqual(len(values), len(ma) + 1)

    def test_MovingAverageComputesCorrectlyForLength2(self):
        l = [0, 2, 0]
        expected = [1, 1]
        result = MovingAverage().evenly_spaced(l, 2)
        self.assertListEqual(expected, result)

    def test_MovingAverageComputesCorrectlyForLength1(self):
        l = [0, 2, 0]
        expected = [0, 2, 0]
        result = MovingAverage().evenly_spaced(l, 1)
        self.assertListEqual(expected, result)

    def test_MovingAverageComputesCorrectlyForLength3(self):
        l = [0, 2, 0]
        expected = [2 / 3]
        result = MovingAverage().evenly_spaced(l, 3)
        self.assertListEqual(expected, result)

    def test_MovingDateAverageWith1DayEvenSpaced(self):
        d = {1: 1, 2: 4, 3: 5}
        expected = {2: 5 / 2, 3: 9 / 2}
        result = MovingAverage().arbitrarily_spaced(d, 2)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpaced(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {3: 13 / 4, 5: 19 / 4}
        result = MovingAverage().arbitrarily_spaced(d, 2)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpacedLength3(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {3: (1 + (1 + 4) / 2 + 4) / 3, 5: (4 + (4 + 5) / 2 + 5) / 3}
        result = MovingAverage().arbitrarily_spaced(d, 3)
        self.assertEqual(expected, result)

    def test_MovingDateAverageWith2DayEvenSpacedLength4(self):
        d = {1: 1, 3: 4, 5: 5}
        expected = {5: (1 + (1 + 4) / 2 + 4 + (4 + 5) / 2 + 5) / 5}
        result = MovingAverage().arbitrarily_spaced(d, 5)
        self.assertEqual(expected, result)



    def test_ema(self):
        alpha = 0.5
        s = [0, 10, 100]
        result = MovingAverage().ema(s, alpha)
        self.assertEqual(s[0], result[0])
        self.assertEqual(s[1], result[1])
        self.assertEqual(s[2], result[2] + 0.5 * result[1])
