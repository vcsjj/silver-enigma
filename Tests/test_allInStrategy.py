from DataSources.Quote import Quote
from Strategies.AllInStrategy import AllInStrategy


def test_generates_one_trade():
    q = [Quote("x", 0, 100, 100, 100, 100, 1)]
    s = AllInStrategy()
    trades = s.Run(budget=1000, symbol="x", quotes=q, start=0, end=100)
    assert 1 == len(trades._tradelist)
    assert 10 == trades._tradelist[0].amount


def test_remainder_is_cash():
    q = [Quote("x", 0, 100, 100, 100, 100, 1)]
    s = AllInStrategy()
    trades = s.Run(budget=1001, symbol="x", quotes=q, start=0, end=100)
    assert 10 == [trade.amount for trade in trades._tradelist if trade.symbol == "x"][0]
    assert 1 == [trade.amount for trade in trades._tradelist if trade.symbol == "cash"][0]

