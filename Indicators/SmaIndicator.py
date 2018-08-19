from Indicators.Indicator import Indicator


class SmaIndicator(Indicator):

    def evenly_spaced(self, data: list, window):

        new_len = len(data) - window + 1
        result = [0] * new_len
        for i in range(0, new_len):
            for j in range(i, i + window):
                result[i] = result[i] + data[j]
            result[i] = result[i] / window
        return result


