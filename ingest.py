from utils.load_documents import load_documents
from utils.text_splitter import split_documents
from utils.vector_store import get_vector_store

print("Loading documents...")

documents = load_documents()

print(f"Pages loaded: {len(documents)}")

chunks = split_documents(documents)

print(f"Chunks created: {len(chunks)}")

vector_store = get_vector_store()

vector_store.add_documents(chunks)

print("Documents successfully stored in ChromaDB!")