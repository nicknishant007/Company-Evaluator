from fastapi import APIRouter
from fastapi import HTTPException

from backend.services.report_service import (
    report_service,
)

router = APIRouter(

    prefix="/report",

    tags=["Report"],

)


@router.get("/{ticker}")

async def get_report(ticker: str):

    report = report_service.get_report(ticker)

    if report is None:

        raise HTTPException(

            status_code=404,

            detail="Report not found",

        )

    return {

        "ticker": ticker,

        "report": report,

    }