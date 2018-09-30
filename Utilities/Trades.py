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

    def value_of_this_stock(self, date, symbol, rate):
        return sum([x.amount * rate for x in self._tradelist if date >= x.date and symbol == x.symbol])

    def value_of_stock(self, date, rate: dict):
        return sum([x.amount*rate[x.symbol] for x in self._tradelist if date >= x.date])

    def possible_profit_of_this_stock(self, date, symbol, rate):
        return sum([(rate - x.rate) * x.amount for x in self._tradelist if date >= x.date and symbol == x.symbol])

    def possible_profit_of_stock(self, date, rate: dict):
        return sum([(rate[x.symbol] - x.rate) * x.amount for x in self._tradelist if date == x.date])
