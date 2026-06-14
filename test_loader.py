from utils.load_documents import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} pages")

print(docs[0].page_content[:500])