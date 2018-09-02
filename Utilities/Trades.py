from Utilities.Trade import Trade


class Trades(object):
    def __init__(self):
        self._tradelist = list()

    def buy(self, trade: Trade):
        if trade.amount < 1:
            raise Exception
        self._tradelist.append(trade)

    def sell(self, trade: Trade):
        if trade.amount > -1:
            raise Exception
        self._tradelist.append(trade)

    def expense(self, date):
        return sum([x.amount * x.rate for x in self._tradelist if date >= x.date and x.amount > 0])

    def revenue(self, date):
        return sum([x.amount * x.rate for x in self._tradelist if date >= x.date and x.amount < 0])
