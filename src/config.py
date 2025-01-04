from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAISettings(BaseSettings):
    api_key: str = "XXX"
    llm: str = "gpt-4o"
    llm_small: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(env_prefix="OPENAI__")


class Settings(BaseSettings):
    openai: OpenAISettings = OpenAISettings()
    debug: bool = False
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
