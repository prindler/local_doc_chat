from langchain_postgres import PGVector
from langchain_core.vectorstores import VectorStore
from ..llm.utils import get_embeddings
from ..config import settings


def get_vector_store() -> VectorStore:
    embeddings = get_embeddings()
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=settings.vectordb.collection,
        connection=settings.vectordb.uri,
        use_jsonb=True,
    )
    return vector_store
