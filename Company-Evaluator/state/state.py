from typing import Any

from typing_extensions import TypedDict


class ReportMetadata(TypedDict):

    recommendation: str

    overall_risk: str


class CompanyState(TypedDict):

    ticker: str

    profile: Any

    stock: Any

    financials: Any

    financial_metrics: Any

    news: Any

    web: Any

    research: Any

    financial_analysis: Any

    risk_analysis: Any

    news_analysis: Any

    valuation_analysis: Any

    report: str

    report_metadata: ReportMetadata

    cleaned_report: str

    parsed_report: Any

    markdown_path: str

    pdf_path: str

    slides_content: Any