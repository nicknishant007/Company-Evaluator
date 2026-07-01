from tavily import TavilyClient

from config.settings import settings


class TavilyDataSource:

    def __init__(self):

        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    async def search_company(
        self,
        company: str,
    ):

        return self.client.search(
            query=f"{company} business overview",
            max_results=5,
        )