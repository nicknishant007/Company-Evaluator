from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Company Evaluator"

    ENV: str = "development"

    HOST: str = "localhost"

    PORT: int = 8000

    DATABASE_URL: str = ("postgresql://postgres:postgres@localhost:5432/company_ai")

    REDIS_URL: str = ("redis://localhost:6379")

    DEFAULT_LLM: str = "mistral"

    QWEN_MODEL:str="qwen/qwen3-14b:free"

    OPENAI_MODEL: str = "gpt-4.1-mini"

    GEMINI_MODEL: str = "gemini-2.5-flash"

    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    MISTRAL_MODEL: str = "mistral-small-latest"

    OPENROUTER_MODEL: str = "tencent/hy3:free"

    LANGSMITH_TRACING:str=""

    LANGSMITH_PROJECT:str=""

    OPENAI_API_KEY: str = ""

    MISTRAL_API_KEY: str = ""

    OLLAMA_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    GOOGLE_API_KEY: str = ""

    OPENROUTER_API_KEY: str = ""

    LANGCHAIN_API_KEY: str = ""

    LANGSMITH_API_KEY: str = ""

    TAVILY_API_KEY: str = ""

    NEWS_API_KEY: str = ""

    FINNHUB_API_KEY: str = ""

    ALPHA_VANTAGE_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()