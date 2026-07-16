# ==========================================================
# VECTOR STORE
# Step 3 of the ingestion pipeline. Embeds text chunks with
# a Sentence-Transformer model and stores them in a FAISS
# index for fast semantic (meaning-based) similarity search.
# ==========================================================

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
# Loaded once at import time (not inside a function) so the
# ~90MB model is only loaded into memory once per app session,
# not once per paper uploaded.

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
    # IndexFlatL2 = brute-force exact search (no approximation).
    # Fine at this scale (a few thousand chunks per session);
    # for a much larger corpus you'd swap this for IndexIVFFlat.

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
    # FAISS returns the indices of the top_k nearest chunks
    # by L2 distance between the query embedding and each
    # stored chunk embedding — this is the actual "search" step.
    
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
