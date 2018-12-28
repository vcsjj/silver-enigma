from DataSources.Quote import Quote
from Strategies.SpacedStrategy import SpacedStrategy


def test_interval_of_trades_is_corect():
    q = [Quote("x", 0, 100, 100, 100, 100, 1), Quote("x", 2, 250, 250, 250, 250, 1)]
    s = SpacedStrategy(spacing = 2, amount = 500)

    trades = s.Run(budget=1000, symbol="x", quotes=q, start=0, end=100)
    assert 2 == len(trades._tradelist)
    assert 5 == [trade.amount for trade in trades._tradelist if trade.date == 0][0]
    assert 2 == [trade.amount for trade in trades._tradelist if trade.date == 2][0]

