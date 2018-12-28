class AbstractStrategy():
    def _correctQuote(self, symbol, quotes, start):
        return [quote for quote in quotes if quote.symbol == symbol and quote.date == start][0]