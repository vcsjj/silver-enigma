class Trade(object):
    date = 0.0
    amount = 0
    symbol = ""
    rate = 0

    def __init__(self, date: float, amount: int, symbol: str, rate: float):
        self.date = date
        self.amount = amount
        self.symbol = symbol
        self.rate = rate

    def __str__(self):
        return str(self.date) + " " + str(self.amount) + " " + str(self.symbol) + " " + str(self.rate)
