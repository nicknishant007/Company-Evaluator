import yfinance as yf

from data_sources.base import (
    BaseDataSource,
)

from data_sources.middleware.retry import (
    retry_on_failure,
)

from data_sources.middleware.cache import (
    cache_response,
)

from schemas.company import (
    CompanyProfile
)

from schemas.stock import (
    StockData
)

from schemas.finance import (
    FinancialData
)

def get_value(df,key,index=0):

    try:

        if key in df.index:

            row=df.loc[key]

            if len(row)>index:

                return row.iloc[index]

    except:

        pass

    return None

class YahooDataSource(BaseDataSource):

    

    #@cache_response(ttl=86400)
    @retry_on_failure()
    async def get_company_profile(self,
             ticker: str):
        company = yf.Ticker(ticker)
        info=company.info
        return CompanyProfile(
            ticker=ticker,
            name=info.get("longName", ""),
            sector=info.get("sector", ""),
            industry=info.get("industry", ""),
            website=info.get("website", ""),
            market_cap=info.get("marketCap", 0.0),
            employee_count=info.get("fullTimeEmployees", 0),
            description=info.get("longBusinessSummary", ""),
        )
    #@cache_response(ttl=300)
    @retry_on_failure()
    async def get_stock_data(
        self,
        ticker: str,
    ):

        company = yf.Ticker(ticker)
        info = company.info

        return StockData(

            ticker=ticker,

            current_price=info.get(
                "currentPrice"),
            fifty_two_week_high=info.get(
                "fiftyTwoWeekHigh"),
            fifty_two_week_low=info.get(
                "fiftyTwoWeekLow"),
            volume=info.get(
                "volume"),
            average_volume=info.get(
                "averageVolume")
        )
    #@cache_response(ttl=86400)
    @retry_on_failure()
    async def get_financials(
    self,
    ticker: str,
    ):

        company = yf.Ticker(ticker)

        income_stmt = company.financials

        balance_sheet = company.balance_sheet

        cashflow = company.cashflow

        return FinancialData(

            ticker=ticker,

            # Income Statement

            total_revenue=get_value(
                income_stmt,
                "Total Revenue"
            ),

            previous_revenue=
            get_value(
                income_stmt,
                "Total Revenue",
                1
            ),

            gross_profit=
            get_value(
                income_stmt,
                "Gross Profit"
            ),

            operating_income=
            get_value(
                income_stmt,
                "Operating Income"
            ),

            net_income=
            get_value(
                income_stmt,
                "Net Income"
            ),

            previous_net_income=
            get_value(
                income_stmt,
                "Net Income",
                1
            ),

            # Balance Sheet

            total_debt=
            get_value(
                balance_sheet,
                "Total Debt"
            ),

            total_equity=
            get_value(
                balance_sheet,
                "Stockholders Equity"
            ),

            current_assets=
            get_value(
                balance_sheet,
                "Current Assets"
            ),

            current_liabilities=
            get_value(
                balance_sheet,
                "Current Liabilities"
            ),

            inventory=
            get_value(
                balance_sheet,
                "Inventory"
            ),

            total_assets=
            get_value(
                balance_sheet,
                "Total Assets"
            ),

            # Cash Flow

            operating_cash_flow=
            get_value(
                cashflow,
                "Operating Cash Flow"
            ),

            capital_expenditure=
            get_value(
                cashflow,
                "Capital Expenditure"
            ),

        )


            