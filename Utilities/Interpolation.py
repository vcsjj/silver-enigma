class Interpolation:
    def create_complete_list(self, d, ma, filled_list, mi):
        i = mi
        while i <= ma:
            if i in d:
                current_key = i
                current_element = d[current_key]
                filled_list.append(current_element)
                i = i + 1
            else:
                overall_delta = 1
                for j in range(i, ma + 1):
                    if j not in d:
                        overall_delta = overall_delta + 1
                    else:
                        filled_list = filled_list + self.fill_empty_between_two_points(d, i, overall_delta)
                        break
                i = i + overall_delta - 1

        return filled_list

    def fill_empty_between_two_points(self, d, first_empty_position, overall_delta):
        new_elements = list()
        delta_now = 1
        while delta_now < overall_delta:
            current_value = self.interpolate(overall_delta, delta_now, d[first_empty_position - 1],
                                             d[first_empty_position + overall_delta - 1])
            new_elements.append(current_value)
            delta_now = delta_now + 1
        return new_elements

    def interpolate(self, overall_delta, delta_now, l, r):
        return l + delta_now * (r - l) / overall_delta
