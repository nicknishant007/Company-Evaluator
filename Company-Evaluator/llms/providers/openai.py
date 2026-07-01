from langchain.chat_models import init_chat_model

from config.settings import settings

def get_openai():
    return init_chat_model(
        model=settings.OPENAI_MODEL,
        api_key=settings.OPENAI_API_KEY,
        model_provider="openai",
        temperature=0.2,
        max_tokens=4096,
        max_retries=4,
        streaming=True
    )