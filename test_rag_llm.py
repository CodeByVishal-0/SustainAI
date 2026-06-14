from agents.rag_agent import answer_question

query = "How can cities become more sustainable?"

response = answer_question(query)

print("\nResponse:\n")
print(response)