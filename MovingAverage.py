from typing import Any, Union


class MovingAverage:
    def evenly_spaced(self, data: list, window):

        new_len = len(data) - window + 1
        result = [0] * new_len
        for i in range(0, new_len):
            for j in range(i, i + window):
                result[i] = result[i] + data[j]
            result[i] = result[i] / window
        return result

    def arbitrarily_spaced(self, d: dict, window):

        keys = list(d.keys())
        mi = min(keys)
        ma = max(keys)
        filled_list = list()

        filled_list = self.create_complete_list(d, ma, filled_list, mi)

        evenly_spaced = self.evenly_spaced(filled_list, window)
        result = dict()
        for key in d:
            if key - window + 1 >= mi:
                result[key] = evenly_spaced[key - mi - window + 1]
        return result

    def create_complete_list(self, d, ma, filled_list, mi):
        for i in range(mi, ma + 1):
            if i in d:
                current_key = i
                current_element = d[current_key]
                filled_list.append(current_element)
            else:
                overall_delta = 1
                for j in range(i, ma + 1):
                    if j not in d:
                        overall_delta = overall_delta + 1
                    else:
                        filled_list = filled_list + self.fill_empty_between_two_points(d, i, overall_delta)
                        break
        return filled_list

    def fill_empty_between_two_points(self, d, first_empty_position, overall_delta):
        new_elements = list()
        delta_now = 1
        while delta_now < overall_delta:
            current_value = self.interpolate(overall_delta, delta_now, d[first_empty_position - 1], d[first_empty_position + overall_delta - 1])
            new_elements.append(current_value)
            delta_now = delta_now + 1
        return new_elements

    def interpolate(self, overall_delta, delta_now, l, r):
        return l + delta_now * (r - l) / overall_delta
