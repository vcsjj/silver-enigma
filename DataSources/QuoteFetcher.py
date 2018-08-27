from typing import NewType
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

from DataSources.Quote import Quote

Date = NewType('Date', float)


class QuoteFetcher(ABC):
    @staticmethod
    def default():
        return InvestopediaQuoteFetcher()

    def fetch(self, symbol: str, start: Date, end: Date):
        return self.get_quotes(self.download(self.create_url(symbol, start, end)))

    def get_quotes(self, data):
        raise NotImplementedError

    def create_url(self, symbol: str, start: Date, end: Date):
        raise NotImplementedError

    @staticmethod
    def download(url):
        f = urllib.request.urlopen(url)
        return f.read()


class InvestopediaQuoteFetcher(QuoteFetcher):
    @staticmethod
    def create_url(symbol: str, start: Date, end: Date):
        formatted_start_date = start.strftime("%b %d, %Y")
        formatted_end_date = end.strftime("%b %d, %Y")
        get_vars = {'Symbol': symbol, 'Type': 'Historical Prices', 'Timeframe': 'Daily',
                    'StartDate': formatted_start_date, 'EndDate': formatted_end_date}

        url = 'https://www.investopedia.com/markets/api/partial/historical/?'
        return url + urllib.parse.urlencode(get_vars)

    def get_quotes(self, html: str):
        rows = list(self.get_table_rows(html))
        return [Quote(r[0], r[1], r[2], r[3], r[4]) for r in rows]

    def get_table_rows(self, html: str):
        bs = BeautifulSoup(html, 'html.parser')
        rows = bs.find_all('tr', attrs={'class': 'in-the-money'})
        for row in rows:
            if is_quote_row(row):
                yield [r.string for r in row.find_all('td')]


def is_quote_row(row):
    return all(is_num_or_date(cell) for
               cell in row.find_all('td'))


def is_num_or_date(cell):
    return cell.has_attr('class') and (cell.attrs['class'][0] == 'num' or cell.attrs['class'][0] == 'date')
