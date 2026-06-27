from rag.pdf_reader import extract_text
from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import store_embeddings

text = extract_text("uploads/A_Review_on_Alzheimers_Disease_Detection_using_Machine_Learning.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

store_embeddings(chunks, embeddings)

print("Embeddings stored successfully!")