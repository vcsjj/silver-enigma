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

#    def value_of_this_stock(self, symbol, date):
#        return sum([x.amount * y.rate for x, y in self._tradelist if date >= x.date and symbol == x.symbol and date == y.date])
#
#    def value_of_stock(self, date):
#        return sum([x.amount * y.rate for x, y in self._tradelist if date >= x.date and date == y.date])
#
#    def possible_profit_of_this_stock(self, date, symbol):
#        return sum([(x.rate-y.rate)*y.amount for x, y in self._tradelist if date == x.date and date >= y.date and symbol == y.symbol])
#
#    def possible_profit_of_stock(self, date):
#        return sum([(x.rate - y.rate) * y.amount for x, y in self._tradelist if date == x.date and date >= y.date])
