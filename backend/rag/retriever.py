import chromadb
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to the database
client = chromadb.PersistentClient(
    path="../database"
)


def retrieve_chunks(question):

    # Get the latest collection
    collection = client.get_collection(
        name="pdf_chunks"
    )

    # Convert question to embedding
    question_embedding = model.encode(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3
    )

    return results["documents"][0]