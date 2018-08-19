from abc import ABC, abstractmethod

from Utilities.Interpolation import Interpolation


class Indicator(ABC):
    __interpolation = Interpolation()

    @abstractmethod
    def evenly_spaced(self, data: list, window):
        pass

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
