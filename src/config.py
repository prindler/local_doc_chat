from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, PostgresDsn


class EmbeddingsSettings(BaseSettings):
    model: str = "text-embedding-3-large"

    model_config = SettingsConfigDict(env_prefix="EMBEDDINGS__")


class LLMSettings(BaseSettings):
    model: str = "gpt-4o"
    model_small: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(env_prefix="LLM__")


class OpenAISettings(BaseSettings):
    api_key: SecretStr

    model_config = SettingsConfigDict(env_prefix="OPENAI__")


class PostgresSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    db: str = "postgres"
    collection: str = "my_docs"
    user: str = "postgres"
    password: SecretStr = "postgres"

    @property
    def uri(self) -> PostgresDsn:
        return f"postgresql+psycopg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}"

    model_config = SettingsConfigDict(env_prefix="POSTGRES__")


class Settings(BaseSettings):
    embeddings: EmbeddingsSettings = EmbeddingsSettings()
    llm: LLMSettings = LLMSettings()
    openai: OpenAISettings = OpenAISettings()
    vectordb: PostgresSettings = PostgresSettings()

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
