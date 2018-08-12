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

        for i in range(mi, ma+1):
            if i in d:
                current_key = i
            current_element = d[current_key]
            filled_list.append(current_element)

        return self.evenly_spaced(filled_list, window)
