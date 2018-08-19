from Interpolation import Interpolation


class MovingAverage:

    __interpolation = Interpolation()

    def ema(self, data: list, alpha):
        return data

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

        filled_list = self.__interpolation.create_complete_list(d, ma, filled_list, mi)

        evenly_spaced = self.evenly_spaced(filled_list, window)
        result = dict()
        for key in d:
            if key - window + 1 >= mi:
                result[key] = evenly_spaced[key - mi - window + 1]
        return result


