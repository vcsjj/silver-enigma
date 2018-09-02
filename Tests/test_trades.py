import pytest

from Utilities.Trade import Trade
from Utilities.Trades import Trades

def test_buyOne_expenseIsOne():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))

    assert 1.0 == t.expense(0.1)

def test_buyOne_expenseIsZeroBeforeBuy():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))

    assert 0.0 == t.expense(date=-1)


def test_buyAtLeastOne():
    t = Trades()
    with pytest.raises(Exception):
        t.buy(Trade(0.0, 0, "S", 1.0))


def test_sellAtLeastOne():
    t = Trades()
    with pytest.raises(Exception):
        t.sell(Trade(0.0, 0, "S", 1.0))


def test_buyOneSellOne_expenseIsOne():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.sell(Trade(1.0, -1, "S", 1.0))

    assert 1.0 == t.expense(2)


def test_buyOneSellOne_revenueIsOne():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.sell(Trade(1.0, -1, "S", 1.0))

    assert 1.0 == t.expense(2)