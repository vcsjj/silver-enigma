from typing import NewType
from abc import ABC, abstractmethod
import urllib.parse

Date = NewType('Date', float)


class QuoteFetcher(ABC):
    def fetch(self, symbol: str, start: Date, end: Date):
        fetchurl = self.create_url(symbol, start, end)

    @abstractmethod
    def create_url(self, symbol: str, start: Date, end: Date):
        pass


class InvestopediaQuoteFetcher(QuoteFetcher):
    def create_url(self, symbol: str, start: Date, end: Date):
        formatted_start_date = start.strftime("%b %d, %Y")
        formatted_end_date = end.strftime("%b %d, %Y")
        get_vars = {'Symbol': symbol, 'Type': 'Historical Prices', 'Timeframe': 'Daily',
                    'StartDate': formatted_start_date, 'EndDate': formatted_end_date}

        url = 'https://www.investopedia.com/markets/api/partial/historical/?'
        return url + urllib.parse.urlencode(get_vars)
