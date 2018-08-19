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

    def test_interpolate(self):
        l = 0
        r = 1
        overall_delta = 2
        delta_now = 1
        expected = 0.5
        result = MovingAverage().interpolate(overall_delta, delta_now, l, r)
        self.assertEqual(expected, result)

    def test_interpolatemore(self):
        l = 0
        r = 1
        overall_delta = 4
        delta_now = 2
        expected = 0.5
        result = MovingAverage().interpolate(overall_delta, delta_now, l, r)
        self.assertEqual(expected, result)

    def test_interpolateleft(self):
        l = 0
        r = 1
        overall_delta = 1
        delta_now = 0
        expected = 0
        result = MovingAverage().interpolate(overall_delta, delta_now, l, r)
        self.assertEqual(expected, result)

    def test_interpolateright(self):
        l = 1
        r = 1
        overall_delta = 1
        delta_now = 0
        expected = 1
        result = MovingAverage().interpolate(overall_delta, delta_now, l, r)
        self.assertEqual(expected, result)

    def test_interpolatenegative(self):
        l = 3
        r = 1
        overall_delta = 2
        delta_now = 1
        expected = 2
        result = MovingAverage().interpolate(overall_delta, delta_now, l, r)
        self.assertEqual(expected, result)

    def test_fill_empty_entries(self):
        d = {0: 5, 7: 10}
        i = 1
        overall_delta = 7
        expected_length = 6
        result = MovingAverage().fill_empty_between_two_points(d, i, overall_delta)
        self.assertEqual(expected_length, len(result))

    def test_fill_empty_entries_value(self):
        d = {0: 0, 10: 10}
        i = 1
        overall_delta = 10
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = MovingAverage().fill_empty_between_two_points(d, i, overall_delta)
        self.assertListEqual(expected_list, result)

    def test_create_complete_list_does_not_add_entries_if_already_full(self):
        d = {0: 0, 1: 10}
        filled_list = list()
        result = MovingAverage().create_complete_list(d, 2, filled_list, 0)
        self.assertListEqual(list(d.values()), result)

    def test_create_complete_list_adds_one_entry(self):
        d = {0: 0, 2: 10}
        filled_list = list()
        result = MovingAverage().create_complete_list(d, 3, filled_list, 0)
        self.assertListEqual([0, 5, 10], result)

    def test_ema(self):
        alpha = 0.5
        s = [0, 10, 100]
        result = MovingAverage().ema(s, alpha)
        self.assertEqual(s[0], result[0])
        self.assertEqual(s[1], result[1])
        self.assertEqual(s[2], result[2] + 0.5 * result[1])
