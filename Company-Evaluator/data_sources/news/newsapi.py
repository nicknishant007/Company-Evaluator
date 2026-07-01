from newsapi import NewsApiClient

from config.settings import settings

from schemas.news import NewsArticle


class NewsDataSource:

    def __init__(self):

        self.client = NewsApiClient(
            api_key=settings.NEWS_API_KEY
        )

    async def get_company_news(
    self,
    company: str,
    limit: int = 10,
    ):

        if not company:

            return []

        response = self.client.get_everything(

            q=f'"{company}"',

            language="en",

            sort_by="publishedAt",

            page_size=limit,
        )

        articles = []

        for article in response["articles"]:

            articles.append(

                NewsArticle(

                    title=article["title"],

                    source=article["source"]["name"],

                    url=article["url"],

                    published_at=article["publishedAt"],

                    description=article["description"],

                )

            )

        return articles