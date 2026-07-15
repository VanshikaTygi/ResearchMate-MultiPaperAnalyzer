import streamlit as st 

# =====================================
# Sidebar UI
# =====================================

def show_sidebar():

    st.title("🤖 ResearchMate")

    st.markdown("---")

    st.markdown("## Navigation")

    if st.button("🏠 Coordinator", use_container_width=True):
        st.session_state.current_page = "Coordinator"

    if st.button("📄 Analysis Agent", use_container_width=True):
        st.session_state.current_page = "Analysis"

    if st.button("🔎 Research Q&A", use_container_width=True):
        st.session_state.current_page = "QA"

    if st.button("📊 Comparison", use_container_width=True):
        st.session_state.current_page = "Comparison"

    if st.button("💡 Innovation", use_container_width=True):
        st.session_state.current_page = "Innovation"

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