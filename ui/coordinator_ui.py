import streamlit as st 

# =====================================
# Coordinator Page
# =====================================

def show_coordinator_page():

    # =====================================
    # Coordinator UI
    # =====================================

    st.markdown("---")

    st.header("🤖 AI Research Coordinator")

    user_query = st.text_area(
        "Ask anything about your uploaded research papers",
        placeholder="Example: Compare both papers and suggest future improvements..."
    )

    analyze_button = st.button("🚀 Analyze")

    return user_query, analyze_button