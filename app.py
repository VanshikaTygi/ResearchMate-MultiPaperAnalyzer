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
uploaded_files = st.file_uploader(
    "Upload Research Paper PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    current_file_names = [
        file.name
        for file in uploaded_files
    ]

    if current_file_names != st.session_state.uploaded_file_names:

        st.session_state.papers = prepare_all_papers(uploaded_files)

        st.session_state.uploaded_file_names = current_file_names

    all_papers = st.session_state.papers

    # paper_names = [
    #     paper["title"]
    #     for paper in all_papers
    # ]

    # selected_paper_name = st.selectbox(
    #     "Select a paper",
    #     paper_names
    # )

    # selected_paper = next(
    #     paper
    #     for paper in all_papers
    #     if paper["title"] == selected_paper_name
    # )


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

            st.write("Selected Agent(s):")
            st.write(", ".join(routing["agents"]))

            st.write("Detected Intent:")
            st.write(", ".join(routing["keys"]))

            for key in routing["keys"]:

                if key == "analysis":

                    if selected_paper["summary"] is None:
                        selected_paper["summary"] = analyze_research_paper(
                            selected_paper["chunks"]
                        )

                    container = show_expert_page("📄 Research Analysis Agent")

                    with container:
                        st.markdown(selected_paper["summary"])


                elif key == "qa":

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
                "Comparison question"
            )

            if st.button("Compare"):

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

            innovation = generate_research_innovation(
                all_papers
            )

            with container:
                st.markdown(innovation)

    # user_query, analyze_button = show_coordinator_page()

    # if analyze_button and user_query:

    #     routing = route_query(user_query)

    #     st.success("Coordinator Decision")

    #     st.write("Selected Agent(s):")
    #     st.write(", ".join(routing["agents"]))

    #     st.write("Detected Intent:")
    #     st.write(", ".join(routing["keys"]))

    #     st.markdown("---")

    #     # Execute selected agents

    #     for key in routing["keys"]:

    #         if key == "analysis":

    #             if selected_paper["summary"] is None:

    #                 selected_paper["summary"] = analyze_research_paper(
    #                     selected_paper["chunks"]
    #                 )

    #             container = show_expert_page("📄 Research Analysis Agent")

    #             with container:
    #                 st.markdown(selected_paper["summary"])


    #         elif key == "qa":

    #             answer = research_qa_agent(
    #                 user_query,
    #                 selected_paper["vector_store"],
    #                 selected_paper["embedding_model"],
    #                 selected_paper["chunks"],
    #                 selected_paper["title"],
    #                 selected_paper["filename"]
    #             )

    #             container = show_expert_page("🔎 Research Q&A Agent")

    #             with container:
    #                 st.markdown(answer)


    #         elif key == "comparison":

    #             if len(all_papers) >= 2:

    #                 comparison = compare_research_papers(

    #                     all_papers,
    #                     user_query

    #                 )

    #                 container = show_expert_page("📊 Comparative Intelligence Agent")

    #                 with container:
    #                     st.markdown(comparison)

    #             else:

    #                 st.warning("Upload at least two papers for comparison.")


    #         elif key == "innovation":

    #             innovation = generate_research_innovation(all_papers)

    #             container = show_expert_page("💡 Research Innovation Agent")

    #             with container:
    #                 st.markdown(innovation)


    # # ==========================
    # # Expert Mode
    # # ==========================

    # st.markdown("---")
    # st.header("🛠 Expert Mode")
    # st.caption(
    #     "Use a specific AI agent when you already know which type of analysis you need."
    # )

    
    # container = show_expert_page("📄 Research Analysis Agent")

    # if st.button("Analyze Research Paper"):

    #     if selected_paper["summary"] is None:

    #         with st.spinner("Analyzing research paper..."):

    #             summary = analyze_research_paper(
    #                 selected_paper["chunks"]
    #             )

    #             selected_paper["summary"] = summary

    #     else:

    #         summary = selected_paper["summary"]

    #     with container:
    #         st.markdown(selected_paper["summary"])


    # container = show_expert_page("🔎 Research Q&A Agent")

    # question = st.text_input(
    # "Ask a question about your research paper"
    # )

    # if question:

    #     answer = research_qa_agent(
    #         question,
    #         selected_paper["vector_store"],
    #         selected_paper["embedding_model"],
    #         selected_paper["chunks"],
    #         selected_paper["title"],
    #         selected_paper["filename"]
    #     )


    #     st.subheader("ResearchMate AI Answer")

    #     with container:
    #         st.markdown(answer)


    # container = show_expert_page("📊 Comparative Intelligence Agent")

    # if len(all_papers) >= 2:

    #     comparison_question = st.text_input(
    #         "Ask a comparison question (leave empty for automatic comparison)"
    #     )

    #     if st.button("Compare Research Papers"):

    #         comparison = compare_research_papers(
    #             all_papers,
    #             comparison_question if comparison_question else None
    #         )

    #         with container:
    #             st.markdown(comparison)

    # else:

    #     st.info("Upload at least 2 research papers for comparison.")

    
    # container = show_expert_page("💡 Research Innovation Agent")

    # if st.button("Generate Research Innovation"):

    #     innovation = generate_research_innovation(all_papers)

    #     st.subheader("Research Innovation Report")

    #     with container:
    #         st.markdown(innovation)