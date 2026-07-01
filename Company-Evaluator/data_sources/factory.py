from data_sources.financial.yahoo import (
    YahooDataSource,
)

from data_sources.news.newsapi import (
    NewsDataSource,
)

from data_sources.web.tavily import (
    TavilyDataSource,
)


class DataSourceFactory:

    @staticmethod
    def yahoo():

        return YahooDataSource()

    @staticmethod
    def news():

        return NewsDataSource()

    @staticmethod
    def tavily():

        return TavilyDataSource()