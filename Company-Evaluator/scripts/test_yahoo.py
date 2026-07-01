import asyncio

from data_sources.financial.yahoo import (
    YahooDataSource
)


async def main():

    yahoo = YahooDataSource()

    profile = (
        await yahoo.get_company_profile(
            "AAPL"
        )
    )

    print(profile)


if __name__ == "__main__":

    asyncio.run(main())