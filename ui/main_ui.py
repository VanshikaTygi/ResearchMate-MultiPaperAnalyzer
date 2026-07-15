import streamlit as st

# =========================
# Hero Section
# =========================

def show_home_header():
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