# ==========================================================
# PAPER MANAGER
# Orchestrates the full per-paper pipeline:
#   extract text -> chunk -> embed -> build FAISS index
# Called once per uploaded file from app.py, and the result
# is stored in st.session_state so it survives Streamlit's
# re-run-on-every-interaction behaviour.
# ==========================================================

from utils.pdf_processor import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_vector_store


def prepare_paper(uploaded_file):
    """
    Process one uploaded research paper and return
    a complete paper dictionary.
    """

    extracted_text = extract_text_from_pdf(uploaded_file)

    chunks = split_text_into_chunks(extracted_text)

    vector_store, embedding_model = create_vector_store(chunks)

    # "summary" starts as None and is filled in lazily —
    # only when the Analysis agent actually runs on this paper.
    # This avoids calling the LLM for every uploaded paper
    # up front, which would waste API quota on papers the
    # user never asks about.

    return {
        "title": uploaded_file.name.replace(".pdf", ""),
        "filename": uploaded_file.name,
        "summary": None,
        "chunks": chunks,
        "vector_store": vector_store,
        "embedding_model": embedding_model
    }


def prepare_all_papers(uploaded_files):
    """
    Process all uploaded research papers.
    """

    papers = []

    for uploaded_file in uploaded_files:
        papers.append(
            prepare_paper(uploaded_file)
        )

    return papers