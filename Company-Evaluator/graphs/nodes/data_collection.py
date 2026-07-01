from data_sources.services.market_data_service import (
    MarketDataService,
)


async def data_collection_node(
    state,
):

    service = MarketDataService()

    result = await service.collect_company_data(
        state["ticker"]
    )

    state["profile"] = result["profile"]

    state["financials"] = result["financials"]

    state["stock"] = result["stock"]

    state["news"] = result["news"]

    state["web"] = result["web"]

    return state