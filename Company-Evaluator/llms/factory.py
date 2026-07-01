from config.settings import settings

from llms.providers.groq import get_groq
from llms.providers.mistral import get_mistral
from llms.providers.openai import get_openai
from llms.providers.gemini import get_gemini
from llms.providers.openrouter_provider import get_openrouter


class LLMFactory:
    @staticmethod
    def get_llm():
        provider = settings.DEFAULT_LLM.lower()
        
        if provider == "groq":
            return get_groq()
        elif provider == "mistral":
            return get_mistral()
        elif provider == "openai":
            return get_openai()
        elif provider == "gemini":
            return get_gemini()
        elif provider == "openrouter":
            return get_openrouter()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")