from langchain.chat_models import init_chat_model

from config.settings import settings

def get_mistral():
    return init_chat_model(
        model=settings.MISTRAL_MODEL,
        api_key=settings.MISTRAL_API_KEY,
        model_provider="mistralai",
        temperature=0.2,
        max_tokens=25000,
        max_retries=4
    )
