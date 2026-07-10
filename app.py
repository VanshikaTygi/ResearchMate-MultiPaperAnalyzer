import streamlit as st
from utils.pdf_processor import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_vector_store, search_vector_store
from agents.qa_agent import research_qa_agent


# Page configuration
st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)


# Application Header
st.title("📚 ResearchMate AI")

st.subheader(
    "Multi-Agent Research Intelligence Assistant"
)


st.write(
    """
    Upload multiple research papers and interact with AI agents
    to analyze papers, compare methodologies, answer questions,
    and discover future research opportunities.
    """
)


# Sidebar
with st.sidebar:
    st.header("ResearchMate Agents")

    st.write("📄 Research Analysis Agent")
    st.write("🔎 Research Q&A Agent")
    st.write("📊 Comparative Intelligence Agent")
    st.write("💡 Research Innovation Agent")


# Main section placeholder
uploaded_file = st.file_uploader(
    "Upload Research Paper PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    extracted_text = extract_text_from_pdf(uploaded_file)

    chunks = split_text_into_chunks(extracted_text)

    st.subheader("Document Processing Result")

    st.success(
        f"PDF processed successfully into {len(chunks)} chunks"
    )

    st.write(chunks[0])


    vector_store, embedding_model = create_vector_store(chunks)

    st.success(
        "Vector database created successfully"
    )

    question = st.text_input(
    "Ask a question about your research paper"
    )

    if question:

        answer = research_qa_agent(
            question,
            vector_store,
            embedding_model,
            chunks
        )


        st.subheader("ResearchMate AI Answer")

        st.write(answer)