from unittest import TestCase

from Utilities.Interpolation import Interpolation


class TestInterpolation(TestCase):

    def test_interpolate(self):
        left = 0
        r = 1
        overall_delta = 2
        delta_now = 1
        expected = 0.5
        result = Interpolation().interpolate(overall_delta, delta_now, left, r)
        self.assertEqual(expected, result)

    def test_interpolate_more(self):
        left = 0
        r = 1
        overall_delta = 4
        delta_now = 2
        expected = 0.5
        result = Interpolation().interpolate(overall_delta, delta_now, left, r)
        self.assertEqual(expected, result)

    def test_interpolate_left(self):
        left = 0
        r = 1
        overall_delta = 1
        delta_now = 0
        expected = 0
        result = Interpolation().interpolate(overall_delta, delta_now, left, r)
        self.assertEqual(expected, result)

    def test_interpolate_right(self):
        left = 1
        r = 1
        overall_delta = 1
        delta_now = 0
        expected = 1
        result = Interpolation().interpolate(overall_delta, delta_now, left, r)
        self.assertEqual(expected, result)

    def test_interpolate_negative(self):
        left = 3
        r = 1
        overall_delta = 2
        delta_now = 1
        expected = 2
        result = Interpolation().interpolate(overall_delta, delta_now, left, r)
        self.assertEqual(expected, result)

    def test_fill_empty_entries(self):
        d = {0: 5, 7: 10}
        i = 1
        overall_delta = 7
        expected_length = 6
        result = Interpolation().fill_empty_between_two_points(d, i, overall_delta)
        self.assertEqual(expected_length, len(result))

    def test_fill_empty_entries_value(self):
        d = {0: 0, 10: 10}
        i = 1
        overall_delta = 10
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = Interpolation().fill_empty_between_two_points(d, i, overall_delta)
        self.assertListEqual(expected_list, result)

    def test_create_complete_list_does_not_add_entries_if_already_full(self):
        d = {0: 0, 1: 10}
        filled_list = list()
        result = Interpolation().create_complete_list(d, 2, filled_list, 0)
        self.assertListEqual(list(d.values()), result)

    def test_create_complete_list_adds_one_entry(self):
        d = {0: 0, 2: 10}
        filled_list = list()
        result = Interpolation().create_complete_list(d, 3, filled_list, 0)
        self.assertListEqual([0, 5, 10], result)
