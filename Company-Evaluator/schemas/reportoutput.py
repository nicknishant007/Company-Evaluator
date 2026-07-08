from typing import Literal

from pydantic import BaseModel


class ReportOutput(BaseModel):

    recommendation: Literal[
        "Strong Buy",
        "Buy",
        "Hold",
        "Sell",
        "Strong Sell",
    ]

    overall_risk: Literal[
        "Low",
        "Moderate",
        "High",
    ]

    report: str