from pydantic import BaseModel


class FinancialMetricsResponse(BaseModel):

    revenue_growth: float | None = None

    net_margin: float | None = None

    roe: float | None = None

    roa: float | None = None

    debt_equity: float | None = None

    free_cash_flow: float | None = None


class AnalyzeResponse(BaseModel):

    company: str

    ticker: str

    industry: str | None = None

    recommendation: str | None = None

    overall_risk: str | None = None

    financial_metrics: FinancialMetricsResponse | None = None

    report: str | None = None

    status: str

    report_url: str

    pdf_url: str

    slides_url: str | None = None