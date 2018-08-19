from unittest import TestCase
import dateutil.parser

from DataSources.QuoteFetcher import *


# noinspection SpellCheckingInspection
class TestQuoteFetcher(TestCase):
    def test_InvestopediaUrl(self):
        symbol = 'MSFT'
        start = dateutil.parser.parse('28.11.2017')
        end = dateutil.parser.parse('5.12.2017')
        expected_url = 'https://www.investopedia.com/markets/api/partial/historical/?Symbol=MSFT&Type=Historical+Prices&Timeframe=Daily&StartDate=Nov+28%2C+2017&EndDate=Dec+05%2C+2017'
        created_url = InvestopediaQuoteFetcher().create_url(symbol, start, end)
        self.assertEqual(expected_url, created_url)

