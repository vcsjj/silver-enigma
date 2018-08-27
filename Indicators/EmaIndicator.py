from Indicators.Indicator import Indicator


class EmaIndicator(Indicator):

    def evenly_spaced(self, data: list, window) -> list:
        alpha = alpha_from_window(window)
        return calculate_with_alpha(data, alpha)[window-1:]


def calculate_with_alpha(data: list, alpha) -> list:
    filled_list = list()
    for i in range(0, len(data)):
        if i == 0:
            filled_list.append(data[0])
        else:
            filled_list.append(alpha * data[i] + (1 - alpha) * filled_list[i - 1])
    return filled_list


def alpha_from_window(window: int) -> float:
    return 2.0/(window + 1)
