from pydantic import BaseModel

class FinancialData(BaseModel):

    ticker: str

    # Income Statement
    total_revenue: float | None = None
    previous_revenue: float | None = None

    gross_profit: float | None = None

    operating_income: float | None = None

    net_income: float | None = None
    previous_net_income: float | None = None

    # Balance Sheet
    total_debt: float | None = None
    total_equity: float | None = None

    current_assets: float | None = None
    current_liabilities: float | None = None

    inventory: float | None = None

    total_assets: float | None = None

    # Cashflow
    operating_cash_flow: float | None = None

    capital_expenditure: float | None = None