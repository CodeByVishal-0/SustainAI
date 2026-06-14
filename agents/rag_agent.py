from utils.vector_store import get_vector_store
from utils.llm import generate_response


def retrieve(query, k=5):
    """
    Retrieve relevant documents from ChromaDB
    """
    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query=query,
        k=k
    )

    return results


def get_context(query):
    """
    Convert retrieved documents into a single context string
    """
    docs = retrieve(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context


def answer_question(query):
    """
    RAG Pipeline:
    Query -> Retrieve -> Generate Answer
    """

    context = get_context(query)

    prompt = f"""
You are SustainAI, an AI Sustainability Assistant.

Use the provided context as the primary source.

If the context contains relevant information:
- Answer clearly
- Mention sustainability insights
- Mention relevant SDGs

If the context is insufficient:
- State that the information was not found in the knowledge base.

Context:
{context}

Question:
{query}
"""

    response = generate_response(prompt)

    return response