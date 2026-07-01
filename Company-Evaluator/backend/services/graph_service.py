from graphs.company_graph import run_graph


class GraphService:

    async def analyze(
        self,
        ticker: str,
    ):

        state = await run_graph(
            ticker
        )

        return state


graph_service = GraphService()