from pydantic import BaseModel


class CompanyProfile(BaseModel):

    ticker: str

    name: str

    sector: str | None = None

    industry: str | None = None

    website: str | None = None

    market_cap: float | None = None

    employee_count: int | None = None

    description: str | None = None