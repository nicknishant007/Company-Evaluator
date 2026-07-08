from fastapi import APIRouter
from fastapi import Depends

from backend.schemas.request import AnalyzeRequest

from backend.schemas.response import AnalyzeResponse,FinancialMetricsResponse

from backend.services.graph_service import graph_service

from backend.api.dependencies import (get_graph_service)


router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"],
)


@router.post(
    "/",
    response_model=AnalyzeResponse,
)
async def analyze_company(

    request: AnalyzeRequest,
    graph_service=Depends(
        get_graph_service
    )

):

    state = await graph_service.analyze(

        request.ticker

    )
    print("\n========== BACKEND RESPONSE ==========\n")

    for key, value in state.items():

        print(f"{key} --> {type(value)}")

    print("\n=====================================\n")
    return AnalyzeResponse(

    company=state["profile"].name,

    ticker=state["ticker"],

    industry=state["profile"].industry,

    recommendation=state["report_metadata"]["recommendation"],          

    overall_risk=state["report_metadata"]["overall_risk"],       

    financial_metrics=FinancialMetricsResponse(

        revenue_growth=state["financial_metrics"].revenue_growth,

        net_margin=state["financial_metrics"].net_margin,

        roe=state["financial_metrics"].roe,

        roa=state["financial_metrics"].roa,

        debt_equity=state["financial_metrics"].debt_equity,

        free_cash_flow=state["financial_metrics"].free_cash_flow,

    ),

    report=state["parsed_report"],

    status="Completed",

    report_url=f"/report/{state['ticker']}",

    pdf_url=f"/pdf/{state['ticker']}",

    slides_url=f"/slides/{state['ticker']}",

)