from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_vector_store(chunks):
    """
    Convert text chunks into embeddings and store them in FAISS vector database
    """

    model = embedding_model

    # Convert chunks into vectors
    embeddings = model.encode(chunks)


    # Find embedding dimension
    dimension = embeddings.shape[1]


    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)


    # Add embeddings into FAISS database
    index.add(
        np.array(embeddings)
    )


    return index, model


def search_vector_store(query, index, model, chunks, top_k=3):
    """
    Search FAISS database and return most relevant chunks
    """

    # Convert user question into embedding
    query_embedding = model.encode([query])


    # Search similar vectors
    distances, results = index.search(
        np.array(query_embedding),
        top_k
    )


    # Get matching chunks
    matched_chunks = []
    matched_indices = []

    for idx in results[0]:
        matched_chunks.append(chunks[idx])
        matched_indices.append(int(idx))


    return matched_chunks, matched_indices
