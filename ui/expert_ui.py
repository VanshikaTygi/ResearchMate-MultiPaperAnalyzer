import streamlit as st

# ==========================================
# Expert Agent UI
# ==========================================

def show_expert_page(title):
    st.markdown("---")

    st.header(title)

    result_container = st.container()

    return result_container