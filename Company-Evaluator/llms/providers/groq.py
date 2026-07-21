from langchain.chat_models import init_chat_model

from config.settings import settings

def get_groq():
    return init_chat_model(
        model=settings.GROQ_MODEL,
        api_key=settings.GROQ_API_KEY,
        model_provider="groq",
        temperature=0.2,
        max_tokens=25000,
        streaming=True,
        max_retries=4
    )