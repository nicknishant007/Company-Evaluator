from pydantic import BaseModel


class FinancialMetrics(BaseModel):

    revenue_growth: float | None = None

    net_income_growth: float | None = None

    gross_margin: float | None = None

    operating_margin: float | None = None

    net_margin: float | None = None

    debt_equity: float | None = None

    current_ratio: float | None = None

    quick_ratio: float | None = None

    roe: float | None = None

    roa: float | None = None

    free_cash_flow: float | None = None