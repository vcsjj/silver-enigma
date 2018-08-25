import pytest

from Indicators.EmaIndicator import EmaIndicator
from Indicators.SmaIndicator import SmaIndicator


@pytest.mark.skip(reason="work in progress")
@pytest.mark.parametrize("window", [2, 3, 4])
def test_ema_equal_sma(window):
    list_both = [1, 2, 3, 4]
    ema_len = len(EmaIndicator().evenly_spaced(list_both, window))
    sma_len = len(SmaIndicator().evenly_spaced(list_both, window))
    assert ema_len == sma_len
