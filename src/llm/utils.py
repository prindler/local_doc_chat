from langchain_core.embeddings import Embeddings
from openai import OpenAI
from ..config import settings


def get_client() -> OpenAI:
    client = OpenAI(api_key=settings.openai.api_key.get_secret_value())

    return client


def get_llm():
    pass


def get_embeddings() -> Embeddings:
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(
        api_key=settings.openai.api_key.get_secret_value(),
        model="text-embedding-3-large",
    )

    return embeddings
