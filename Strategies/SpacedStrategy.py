from Strategies.AbstractStrategy import AbstractStrategy
from Utilities.Trade import Trade
from Utilities.Trades import Trades


class SpacedStrategy(AbstractStrategy):
    def __init__(self, spacing, amount):
        self._spacing = spacing
        self._amount = amount

    def Run(self, budget, symbol, quotes, start, end):
        repeat = int(budget/self._amount)
        t = Trades()
        for i in range(repeat):

            time = start + i * self._spacing
            correct_quote = self._correctQuote(symbol, quotes, time)
            average_rate = ((correct_quote.high + correct_quote.low) / 2)
            integralAmount = int(self._amount / average_rate)
            t.buy(Trade(time, integralAmount, symbol, average_rate))
            if(integralAmount * average_rate != self._amount):
                t.buy(Trade(time, -integralAmount * average_rate + self._amount, "cash", 1.0))

        return t