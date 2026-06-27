from rag.retriever import retrieve_chunks

question = input("Ask a question: ")

results = retrieve_chunks(question)

print("\nRelevant Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"Chunk {i}")
    print("-" * 40)
    print(chunk)
    print()