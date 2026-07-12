import streamlit as st
from utils.pdf_processor import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_vector_store, search_vector_store
from agents.qa_agent import research_qa_agent
from agents.analysis_agent import analyze_research_paper
from agents.comparison_agent import compare_research_papers


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
uploaded_files = st.file_uploader(
    "Upload Research Paper PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    all_papers = []

    for uploaded_file in uploaded_files:

        extracted_text = extract_text_from_pdf(uploaded_file)

        chunks = split_text_into_chunks(extracted_text)

        vector_store, embedding_model = create_vector_store(chunks)

        analysis = analyze_research_paper(chunks)

        paper_data = {
            "title": uploaded_file.name.replace(".pdf", ""),
            "filename": uploaded_file.name,
            "summary": analysis,
            "chunks": chunks,
            "vector_store": vector_store,
            "embedding_model": embedding_model
        }

        all_papers.append(paper_data)

    paper_names = [
        paper["title"]
        for paper in all_papers
    ]

    selected_paper_name = st.selectbox(
        "Select a paper",
        paper_names
    )

    selected_paper = next(
        paper
        for paper in all_papers
        if paper["title"] == selected_paper_name
    )


    st.subheader("Research Analysis Agent")

    if st.button("Analyze Research Paper"):
        st.write(selected_paper["summary"])


    question = st.text_input(
    "Ask a question about your research paper"
    )

    if question:

        answer = research_qa_agent(
            question,
            selected_paper["vector_store"],
            selected_paper["embedding_model"],
            selected_paper["chunks"]
        )


        st.subheader("ResearchMate AI Answer")

        st.write(answer)


    st.subheader("Comparative Intelligence Agent")

    if len(all_papers) >= 2:

        comparison_question = st.text_input(
            "Ask a comparison question (leave empty for automatic comparison)"
        )

        if st.button("Compare Research Papers"):

            comparison = compare_research_papers(
                all_papers,
                comparison_question if comparison_question else None
            )

            st.write(comparison)

    else:

        st.info("Upload at least 2 research papers for comparison.")