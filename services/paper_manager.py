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