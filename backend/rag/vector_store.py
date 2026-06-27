import chromadb

client = chromadb.PersistentClient(
    path="../database"
)


def store_embeddings(chunks, embeddings):

    # Delete the old collection if it exists
    try:
        client.delete_collection("pdf_chunks")
    except:
        pass

    # Create a fresh collection
    collection = client.create_collection(
        name="pdf_chunks"
    )

    # Create unique IDs
    ids = []

    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")

    # Store everything
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )