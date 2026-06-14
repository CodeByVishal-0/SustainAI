from agents.rag_agent import get_context

query = "How can cities become more sustainable?"

context = get_context(query)

print(context[:2000])