import datetime
from unittest import TestCase
import dateutil.parser

from DataSources.QuoteFetcher import *


# noinspection SpellCheckingInspection
class TestQuoteFetcher(TestCase):
    def test_InvestopediaUrl(self):
        symbol = 'MSFT'
        start = datetime.date(2017, 11, 28)
        end = datetime.date(2017, 12, 5)

        # expected = 'https://www.investopedia.com/markets/api/partial/historical/?Symbol=MSFT&Type=Historical' \
        #               '+Prices&Timeframe=Daily&StartDate=Nov+28%2C+2017&EndDate=Dec+05%2C+2017 '

        created = InvestopediaQuoteFetcher().create_url(symbol, start, end)

        urlparse = urllib.parse.urlparse(created)
        actual_query = urllib.parse.parse_qs(urlparse.query)

        self.assertEqual('Nov 28, 2017', actual_query['StartDate'][0])
        self.assertEqual('Dec 05, 2017', actual_query['EndDate'][0])
        self.assertEqual('MSFT', actual_query['Symbol'][0])
        self.assertEqual('Historical Prices', actual_query['Type'][0])
        self.assertEqual('Daily', actual_query['Timeframe'][0])
        self.assertEqual('https', urlparse.scheme)
        self.assertEqual('www.investopedia.com', urlparse.netloc)
        self.assertEqual('/markets/api/partial/historical/', urlparse.path)
