from utils.vector_store import get_vector_store

vector_store = get_vector_store()

results = vector_store.similarity_search(
    "How can cities become more sustainable?",
    k=3
)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 50)
    print(doc.page_content[:500])
    