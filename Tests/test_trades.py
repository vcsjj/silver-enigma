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


def test_buyOneSellOne_revenueIsminusOne():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.sell(Trade(1.0, -1, "S", 1.0))

    assert -1.0 == t.revenue(2)


def test_buyOnesellOne_sameDate():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.sell(Trade(0.0, -1, "S", 1.0))

    assert 0.0 == t.expense(1) + t.revenue(1)


def test_buyTwodifferent_expenseTwo():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.buy(Trade(0.0, 1, "D", 1.0))

    assert 2.0 == t.expense(1)


def test_expensebeforelastTrade():
    t = Trades()
    t.buy(Trade(0.0, 1, "S", 1.0))
    t.buy(Trade(1.0, 1, "S", 1.0))

    assert 1.0 == t.expense(0.1)

def test_sellTwodifferent_revenueminusTwo():
    t = Trades()
    t.sell(Trade(0.0, -1, "S", 1.0))
    t.sell(Trade(0.0, -1, "D", 1.0))

    assert -2.0 == t.revenue(1)


def test_revenuebeforelastTrade():
    t = Trades()
    t.sell(Trade(0.0, -1, "S", 1.0))
    t.sell(Trade(1.0, -1, "S", 1.0))

    assert -1.0 == t.revenue(0.1)

def test_value_of_this_stock():
    t = Trades()
    t.buy(Trade(0.0, 1, "x", 2.0))

    assert t.value_of_this_stock(1.0, "x", 2.1) == 2.1

def test_increasingrate_doublebuy():
    t = Trades()
    t.buy(Trade(0.0, 1, "x", 1.0))
    t.buy(Trade(1.0, 1, "x", 2.0))

    assert t.value_of_this_stock(1.5, "x", 2.0) == 4.0

def test_possible_profit_of_this_stock():
    t = Trades()
    t.buy(Trade(0.0, 1, "x", 1.0))
    t.buy(Trade(1.0, 1, "x", 2.0))

    assert t.possible_profit_of_this_stock(1.5, "x", 2.0) == 1.0
