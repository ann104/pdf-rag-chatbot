from rag.pdf_reader import extract_text
from rag.chunker import chunk_text
from rag.embedder import create_embeddings

# Read PDF
text = extract_text("uploads/A_Review_on_Alzheimers_Disease_Detection_using_Machine_Learning.pdf")

# Split into chunks
chunks = chunk_text(text)

# Generate embeddings
embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Length of one embedding:", len(embeddings[0]))