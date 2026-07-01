from data_sources.factory import (
    DataSourceFactory,
)


class MarketDataService:

    def __init__(self):

        self.yahoo = (
            DataSourceFactory.yahoo()
        )

        self.news = (
            DataSourceFactory.news()
        )

        self.tavily = (
            DataSourceFactory.tavily()
        )

    async def collect_company_data(
        self,
        ticker: str,
    ):

        profile = (
            await self.yahoo
            .get_company_profile(
                ticker
            )
        )
        company_name=profile.name
        print(company_name)
        if not company_name:
            company_name=ticker

        stock = (
            await self.yahoo
            .get_stock_data(
                ticker
            )
        )

        financials=( 
            await self.yahoo.get_financials(
                ticker
            )
        )

        news = (
            await self.news
            .get_company_news(
                profile.name
            )
        )

        web = (
            await self.tavily
            .search_company(
                profile.name
            )
        )

        return {

            "profile": profile,

            "stock": stock,

            "financials":financials,

            "news": news,

            "web": web,
        }