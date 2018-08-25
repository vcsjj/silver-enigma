import datetime
from unittest import TestCase
from unittest import mock
from pytest_mock import MockFixture

from DataSources.QuoteFetcher import *


# noinspection SpellCheckingInspection
class TestQuoteFetcher(TestCase):
    html = """<div class="page">
<table class="data">
    <tbody data-rows="7" data-start-date="Nov 28, 2017">
    <tr class="header-row">
        <th class="date">Date</th>
        <th class="num">Open</th>
        <th class="num">High</th>
        <th class="num">Low</th>
        <th class="num">Adj. Close</th>
        <th class="num">Volume</th>
    </tr>

        <tr class="in-the-money">
        <td class="date">Dec 05, 2017</td>
                <td class="num">178.58</td>
        <td class="num">185.30</td>
        <td class="num">174.41</td>
        <td class="num">179.11</td>
        <td class="num">5,164,761</td>
            </tr>
                <tr class="in-the-money">
        <td class="date">Dec 05, 2017</td>
                <td class="text" colspan="5" align="center">0.50 Dividend</td>
            </tr>
                <tr class="in-the-money">
        <td class="date">Dec 04, 2017</td>
                <td class="num">187.67</td>
        <td class="num">187.82</td>
        <td class="num">177.59</td>
        <td class="num">178.82</td>
        <td class="num">5,351,766</td>
            </tr>
                <tr class="in-the-money">
        <td class="date">Dec 01, 2017</td>
                <td class="num">187.98</td>
        <td class="num">189.24</td>
        <td class="num">178.77</td>
        <td class="num">185.81</td>
        <td class="num">5,659,574</td>
            </tr>
                <tr class="in-the-money">
        <td class="date">Nov 30, 2017</td>
                <td class="num">195.31</td>
        <td class="num">196.62</td>
        <td class="num">189.28</td>
        <td class="num">190.29</td>
        <td class="num">5,047,672</td>
            </tr>
                <tr class="in-the-money">
        <td class="date">Nov 29, 2017</td>
                <td class="num">209.40</td>
        <td class="num">209.61</td>
        <td class="num">187.25</td>
        <td class="num">192.57</td>
        <td class="num">7,980,992</td>
            </tr>
            <tr class="in-the-money"> 
        <td class="date">Nov 28, 2017</td>
                <td class="num">209.38</td>
        <td class="num">213.10</td>
        <td class="num">207.50</td>
        <td class="num">210.88</td>
        <td class="num">2,496,619</td>
            </tr> 
             </tbody>
</table>
    </div>
"""

    def test_tableItemsHaveCorrectValue(self):
        quotes = InvestopediaQuoteFetcher().get_table_items(self.html)
        self.assertEqual('187.98', quotes[2].open)

    def test_fetchesRowsOfTable(self):
        rows = InvestopediaQuoteFetcher().get_table_rows(self.html)
        self.assertEqual(6, len(list(rows)))

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


def test_fetches_supplied_url(mocker: MockFixture):
    # arrange
    page_content = 'some content'
    reader = mock.Mock(**{'read.return_value': page_content})
    mocker.patch('urllib.request.urlopen', **{'return_value': reader})

    # act
    url = 'https://www.investopedia.com/markets/api/partial/historical/?Symbol=MSFT&Type=Historical' \
          '+Prices&Timeframe=Daily&StartDate=Nov+28%2C+2017&EndDate=Dec+05%2C+2017 '
    html_content = InvestopediaQuoteFetcher().download(url)

    # assert
    urllib.request.urlopen.assert_called_once_with(url)
    assert html_content == page_content
