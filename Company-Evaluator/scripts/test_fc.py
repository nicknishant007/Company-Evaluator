import asyncio

from data_sources.financial.yahoo import YahooDataSource
from financial_engine.calculator import FinancialCalculator


async def main():

    datasource = YahooDataSource()

    financials = await datasource.get_financials(
        "AAPL"
    )

    calculator = FinancialCalculator()

    metrics = calculator.calculate(
        financials
    )

    print(metrics.model_dump())


asyncio.run(main())