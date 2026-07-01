from langchain.chat_models import init_chat_model

from config.settings import settings


def get_openrouter():

    return init_chat_model(

        api_key=settings.OPENROUTER_API_KEY,

        base_url="https://openrouter.ai/api/v1",

        model=settings.OPENROUTER_MODEL,

        temperature=0.2,
    )