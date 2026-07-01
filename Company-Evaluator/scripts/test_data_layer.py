import asyncio

from data_sources.services.market_data_service import (
    MarketDataService,
)


async def main():

    service = (
        MarketDataService()
    )

    result = await (
        service.collect_company_data(
            "AAPL"
        )
    )

    print(result)


if __name__ == "__main__":

    asyncio.run(main())