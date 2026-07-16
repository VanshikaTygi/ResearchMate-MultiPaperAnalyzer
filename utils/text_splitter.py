# ==========================================================
# TEXT SPLITTER
# Step 2 of the ingestion pipeline. Breaks one long paper
# string into overlapping ~1000-character chunks so that:
#   (a) each chunk is small enough to embed meaningfully
#   (b) the 200-char overlap prevents losing context that
#       falls right on a chunk boundary
# ==========================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text_into_chunks(text):
    """
    Split extracted research paper text into smaller chunks
    """

    # chunk_size=1000, overlap=200 was chosen as a balance:
    # smaller chunks -> more precise retrieval but less context per chunk.
    # larger chunks -> more context but noisier semantic search.
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks
