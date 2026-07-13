import streamlit as st
from utils.pdf_processor import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_vector_store, search_vector_store
from agents.qa_agent import research_qa_agent
from agents.analysis_agent import analyze_research_paper
from agents.comparison_agent import compare_research_papers
from agents.innovation_agent import generate_research_innovation
from agents.coordinator_agent import route_query


# Page configuration
st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)


# =========================
# Hero Section
# =========================

st.title("📚 ResearchMate AI")

st.markdown(
    """
### Multi-Agent Research Intelligence Platform

Analyze, compare and understand multiple research papers using
specialized AI agents powered by Retrieval-Augmented Generation (RAG),
semantic search and Large Language Models.

Upload one or multiple research papers to:

- 📄 Generate structured paper analysis
- 🔎 Ask intelligent research questions
- 📊 Compare multiple papers
- 💡 Discover research gaps and innovation opportunities

---
"""
)


# Sidebar
with st.sidebar:

    st.title("🤖 ResearchMate")

    st.markdown("---")

    st.markdown("## Available AI Agents")

    st.success("📄 Research Analysis Agent")

    st.info("🔎 Research Q&A Agent")

    st.warning("📊 Comparative Intelligence Agent")

    st.error("💡 Research Innovation Agent")

    st.markdown("---")

    st.markdown("### Project Features")

    st.markdown("""
    - 📑 Multi-PDF Upload
    - 🧠 LLM Powered
    - 🔍 Semantic Search
    - 📚 FAISS Vector Database
    - 🤖 Multi-Agent Architecture
    - 💡 Research Gap Discovery
    """)

    st.markdown("---")

    st.caption("ResearchMate AI v1.0")


st.info(
"""
📄 **Upload one or more research papers**

Supported format:
- PDF (.pdf)

Capabilities:
- Multiple PDF upload
- Automatic text extraction
- Semantic indexing
- AI-powered analysis
- Cross-paper comparison
"""
)

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


    # ==========================
    # Coordinator
    # ==========================

    st.markdown("---")

    st.header("🤖 AI Research Coordinator")

    user_query = st.text_area(
        "Ask anything about your uploaded research papers",
        placeholder="Example: Compare both papers and suggest future improvements..."
    )

    analyze_button = st.button("🚀 Analyze")

    if analyze_button and user_query:

        routing = route_query(user_query)

        st.success("Coordinator Decision")

        st.write("Selected Agent(s):")
        st.write(", ".join(routing["agents"]))

        st.write("Detected Intent:")
        st.write(", ".join(routing["keys"]))

        st.markdown("---")

        # Execute selected agents

        for key in routing["keys"]:

            if key == "analysis":

                st.subheader("📄 Research Analysis Agent")

                st.write(selected_paper["summary"])


            elif key == "qa":

                answer = research_qa_agent(

                    user_query,
                    selected_paper["vector_store"],
                    selected_paper["embedding_model"],
                    selected_paper["chunks"]

                )

                st.subheader("🔍 Research Q&A Agent")

                st.write(answer)


            elif key == "comparison":

                if len(all_papers) >= 2:

                    comparison = compare_research_papers(

                        all_papers,
                        user_query

                    )

                    st.subheader("📊 Comparative Intelligence Agent")

                    st.write(comparison)

                else:

                    st.warning("Upload at least two papers for comparison.")


            elif key == "innovation":

                innovation = generate_research_innovation(all_papers)

                st.subheader("💡 Innovation Suggestions Agent")

                st.write(innovation)


    # ==========================
    # Expert Mode
    # ==========================

    st.markdown("---")
    st.header("🛠 Expert Mode")
    st.caption(
        "Use a specific AI agent when you already know which type of analysis you need."
    )

    st.subheader("📄 Research Analysis Agent")

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

    
    st.subheader("Research Innovation Agent")

    if st.button("Generate Research Innovation"):

        innovation_report = generate_research_innovation(all_papers)

        st.subheader("Research Innovation Report")

        st.write(innovation_report)