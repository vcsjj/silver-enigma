from typing import NewType
from abc import ABC, abstractmethod

Date = NewType('Date', float)


class QuoteFetcher(ABC):
    def fetch(self, symbol: str, start: Date, end: Date):
        fetchurl = self.create_url(symbol, start, end)

    @abstractmethod
    def create_url(self, symbol: str, start: Date, end: Date):
        pass


class InvestopediaQuoteFetcher(QuoteFetcher):
    def create_url(self, symbol: str, start: Date, end: Date):
        pass
