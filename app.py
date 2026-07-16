import streamlit as st
from services.paper_manager import prepare_all_papers
from utils.vector_store import search_vector_store
from agents.qa_agent import research_qa_agent
from agents.analysis_agent import analyze_research_paper
from agents.comparison_agent import compare_research_papers
from agents.innovation_agent import generate_research_innovation
from agents.coordinator_agent import route_query
import time
from ui.main_ui import show_home_header
from ui.sidebar_ui import show_sidebar
from ui.coordinator_ui import show_coordinator_page
from ui.expert_ui import show_expert_page


# Page configuration
st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.main{ background:#F7F9FC; }

section[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:1px solid #E5E7EB;
}
            
section[data-testid="stSidebar"] .stButton>button{
    font-size:15px;
}
section[data-testid="stSidebar"] p{
    font-size:13.5px;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    border:1px solid #dbe2ef;
    padding:10px;
    font-weight:600;
    transition:0.2s;
}
.stButton>button:hover{
    border:1px solid #2563EB;
    color:#2563EB;
    transform:scale(1.02);
}

[data-testid="stFileUploader"]{
    border:2px dashed #2563EB;
    border-radius:12px;
    padding:20px;
    background:#FAFBFF;
}

.stSuccess, .stInfo, .stWarning{ border-radius:10px; }
textarea{ border-radius:10px !important; }
div[data-baseweb="select"]{ border-radius:10px; }
h1,h2,h3{ color:#111827; }

[data-testid="stChatInput"]{
    border-radius:14px;
    border:1px solid #dbe2ef;
}
</style>
""", unsafe_allow_html=True)


if "papers" not in st.session_state:
    st.session_state.papers = []

if "uploaded_file_names" not in st.session_state:
    st.session_state.uploaded_file_names = []

# =====================================
# Current Active Page
# =====================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Coordinator"


# Hero Section
show_home_header()


# Sidebar
with st.sidebar:
    show_sidebar()


# =====================================
# Page Routing
# =====================================

current_page = st.session_state.current_page


# Main section placeholder

with st.container(border=True):
    st.markdown("""
    ## 📂 Upload Research Papers

    Upload one or multiple research papers.

    **Supported Format:** PDF &nbsp;•&nbsp; **Maximum Size:** 200 MB &nbsp;•&nbsp; Multiple uploads supported.
    """)

    uploaded_files = st.file_uploader(
        "Upload Research Paper PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    MAX_PAPERS = 6

    if uploaded_files and len(uploaded_files) > MAX_PAPERS:
        st.warning(
            f"⚠️ You've selected {len(uploaded_files)} papers. To avoid API rate-limit errors, "
            f"only the first {MAX_PAPERS} will be processed. Consider analyzing papers in smaller batches."
        )
        uploaded_files = uploaded_files[:MAX_PAPERS]


    if uploaded_files:
        st.markdown(f"""
        <div style="display:flex;gap:16px;margin-top:10px;">
            <div style="background:#EEF2FF;color:#4F46E5;padding:6px 14px;border-radius:8px;font-size:13px;font-weight:600;">
                📎 {len(uploaded_files)} file(s) ready
            </div>
        </div>
        """, unsafe_allow_html=True)


if uploaded_files:

    current_file_names = [
        file.name
        for file in uploaded_files
    ]

    if current_file_names != st.session_state.uploaded_file_names:
    
        st.toast(f"{len(uploaded_files)} paper(s) uploaded successfully.")

        with st.spinner("Reading and indexing your paper(s)... this can take a moment for larger PDFs."):
            st.session_state.papers = prepare_all_papers(uploaded_files)

        st.session_state.uploaded_file_names = current_file_names

    all_papers = st.session_state.papers


    # ==========================
    # Coordinator
    # ==========================

    # =====================================
    # PAGE ROUTER
    # =====================================

    if current_page == "Coordinator":

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


        user_query, analyze_button = show_coordinator_page()

        if analyze_button and user_query:

            routing = route_query(user_query)

            st.success("Coordinator Decision")

            st.write("Selected Agent(s): " + ", ".join(routing["agents"]))

            st.write("Detected Intent: " + ", ".join(routing["keys"]))

            for key in routing["keys"]:

                if key == "analysis":

                    if selected_paper["summary"] is None:
                        with st.spinner("Analyzing the paper..."):
                            selected_paper["summary"] = analyze_research_paper(
                                selected_paper["chunks"]
                            )

                    container = show_expert_page("📄 Research Analysis Agent")

                    with container:
                        st.markdown(selected_paper["summary"])


                elif key == "qa":

                    with st.spinner("Searching the paper for your answer..."):
                        answer = research_qa_agent(
                            user_query,
                            selected_paper["vector_store"],
                            selected_paper["embedding_model"],
                            selected_paper["chunks"],
                            selected_paper["title"],
                            selected_paper["filename"]
                        )

                    container = show_expert_page("🔎 Research Q&A Agent")

                    with container:
                        st.markdown(answer)


                elif key == "comparison":

                    if len(all_papers) >= 2:

                        with st.spinner("Comparing the uploaded papers..."):
                            comparison = compare_research_papers(
                                all_papers,
                                user_query
                            )

                        container = show_expert_page("📊 Comparative Intelligence Agent")

                        with container:
                            st.markdown(comparison)

                    else:

                        st.warning("Upload at least two papers.")


                elif key == "innovation":

                    with st.spinner("Identifying research gaps and future directions..."):
                        innovation = generate_research_innovation(all_papers)

                    container = show_expert_page("💡 Research Innovation Agent")

                    with container:
                        st.markdown(innovation)


    elif current_page == "Analysis":

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

        container = show_expert_page("📄 Research Analysis Agent")

        if st.button("Analyze Research Paper"):

            if selected_paper["summary"] is None:

                with st.spinner("Analyzing the paper..."):
                    selected_paper["summary"] = analyze_research_paper(
                        selected_paper["chunks"]
                    )

            with container:
                st.markdown(selected_paper["summary"])


    elif current_page == "QA":

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

        container = show_expert_page("🔎 Research Q&A Agent")

        question = st.text_input(
            "Ask a question"
        )

        if question:

            with st.spinner("Searching the paper for your answer..."):
                answer = research_qa_agent(
                    question,
                    selected_paper["vector_store"],
                    selected_paper["embedding_model"],
                    selected_paper["chunks"],
                    selected_paper["title"],
                    selected_paper["filename"]
                )

            with container:
                st.markdown(answer)


    elif current_page == "Comparison":

        container = show_expert_page("📊 Comparative Intelligence Agent")

        if len(all_papers) >= 2:

            comparison_question = st.text_input(
                "Comparison question (optional)",
                placeholder="Leave empty for an automatic full comparison"
            )

            if st.button("Compare"):

                with st.spinner("Comparing the uploaded papers..."):
                    comparison = compare_research_papers(
                        all_papers,
                        comparison_question if comparison_question else None
                    )

                with container:
                    st.markdown(comparison)

        else:

            st.info("Upload at least 2 papers.")


    elif current_page == "Innovation":

        container = show_expert_page("💡 Research Innovation Agent")

        if st.button("Generate Innovation"):

            with st.spinner("Identifying research gaps and future directions..."):
                innovation = generate_research_innovation(
                    all_papers
                )

            with container:
                st.markdown(innovation)