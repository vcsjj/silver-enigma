from Indicators.EmaIndicator import calculate_with_alpha, alpha_from_window
import pytest


def test_calculate_with_alpha():
    alpha = 0.5
    y = [0, 10, 100]
    result = calculate_with_alpha(y, alpha)
    assert y[0] == result[0]
    assert alpha * y[1] + (1 - alpha) * result[0] == result[1]
    assert alpha * y[2] + (1 - alpha) * result[1] == result[2]


@pytest.mark.parametrize('n, alpha', [(1, 1), (10, 2.0 / 11.0)])
def test_alpha_to_n_ratio(n, alpha):
    assert alpha_from_window(n) == alpha
