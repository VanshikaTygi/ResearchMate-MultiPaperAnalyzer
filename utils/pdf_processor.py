# ==========================================================
# PDF PROCESSOR
# Converts an uploaded PDF (Streamlit UploadedFile object)
# into a single plain-text string. This is step 1 of the
# ingestion pipeline: PDF -> text -> chunks -> embeddings.
# ==========================================================


import fitz


# PyMuPDF loads the PDF page-by-page; we concatenate all
# page text into one string. Page boundaries are NOT
# preserved here — if you ever need page numbers for
# citations, this is the place to start tracking them.


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded research paper PDF
    """

    text = ""

    pdf_document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    for page in pdf_document:
        text += page.get_text()

    return text