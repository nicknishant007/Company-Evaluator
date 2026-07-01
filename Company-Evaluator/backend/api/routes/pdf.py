from fastapi import APIRouter
from fastapi import HTTPException

from fastapi.responses import FileResponse

from backend.services.pdf_service import (
    pdf_service,
)

router = APIRouter(

    prefix="/pdf",

    tags=["PDF"],

)


@router.get("/{ticker}")

async def download_pdf(

    ticker: str,

):

    pdf = pdf_service.get_pdf(

        ticker

    )

    if pdf is None:

        raise HTTPException(

            status_code=404,

            detail="PDF not found",

        )

    return FileResponse(

        pdf,

        media_type="application/pdf",

        filename=pdf.name,

    )