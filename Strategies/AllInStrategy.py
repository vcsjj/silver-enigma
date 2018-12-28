from Strategies.AbstractStrategy import AbstractStrategy
from Utilities.Trade import Trade
from Utilities.Trades import Trades


class AllInStrategy(AbstractStrategy):
    def Run(self, budget, symbol, quotes, start, end):
        correct_quote = self._correctQuote(symbol, quotes, start)
        average_rate = ((correct_quote.high + correct_quote.low) / 2)
        t = Trades()
        integralAmount = int(budget / average_rate)
        t.buy(Trade(start, integralAmount, symbol, average_rate))
        if(integralAmount * average_rate != budget):
            t.buy(Trade(start, -integralAmount * average_rate + budget, "cash", 1.0))

        return t
