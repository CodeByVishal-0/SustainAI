from langchain_chroma import Chroma
from utils.embedding import get_embedding_model

def get_vector_store():

    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name="sustainability_docs",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store