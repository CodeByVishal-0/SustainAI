from utils.load_documents import load_documents
from utils.text_splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print(f"Total chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:\n")
print(chunks[0].metadata)