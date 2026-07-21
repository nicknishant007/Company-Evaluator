from langchain_openai import ChatOpenAI

from config.settings import settings
def get_kimi():
    return ChatOpenAI(
        model=settings.KIMI_MODEL,
        base_url="https://api.moonshot.ai/v1",
        api_key=settings.KIMI_API_KEY,
        temperature=0.2,
        max_tokens=25000,
        max_retries=3
    )