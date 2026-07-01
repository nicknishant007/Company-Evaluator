from graphs.builder import (
    company_graph,
)

from state.state import (
    CompanyState,
)


async def run_graph(
    ticker: str,
):

    state = CompanyState(
        ticker=ticker,
    )

    result = await company_graph.ainvoke(
        state
    )

    return result