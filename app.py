import streamlit as st


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
st.info(
    "🚀 Upload and AI analysis features coming soon."
)