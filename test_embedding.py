from utils.embedding import get_embedding_model

embeddings = get_embedding_model()

vector = embeddings.embed_query(
    "How can I reduce electricity consumption?"
)

print(f"Vector Size: {len(vector)}")
print(vector[:5])