from langchain.chat_models import init_chat_model

from config.settings import settings

def get_gemini():
    return init_chat_model(
        model=settings.GEMINI_MODEL,
        api_key=settings.GOOGLE_API_KEY,
        model_provider="google_genai",
        temperature=0.2,
        max_tokens=16000,
        streaming=True,
        max_retries=4
    )
