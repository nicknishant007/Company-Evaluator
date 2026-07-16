from langchain_openai import ChatOpenAI

from config.settings import settings
def get_qwen():
    return ChatOpenAI(
        model=settings.QWEN_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.2,
        max_tokens=18000,
        max_retries=4
    )