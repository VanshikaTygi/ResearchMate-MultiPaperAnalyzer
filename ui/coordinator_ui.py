# ==========================================================
# COORDINATOR CHAT UI
# Renders the ChatGPT-style chat box used on the Coordinator
# page. Returns (user_query, analyze_button) back to app.py,
# which then calls route_query() on that text.
# ==========================================================

import streamlit as st

def show_coordinator_page():
    st.markdown("""
    <div style="
        border-left: 4px solid #4F46E5;
        background: #EEF2FF;
        padding: 14px 18px;
        border-radius: 10px;
        margin: 24px 0 16px 0;
    ">
        <span style="font-size:22px;font-weight:700;color:#111827;">🤖 AI Research Coordinator</span>
        <div style="font-size:13px;color:#4B5563;margin-top:4px;">Ask anything — I'll route your question to the right specialist agent automatically.</div>
    </div>
    """, unsafe_allow_html=True)

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(
            "Hi! I'm the **Coordinator Agent**. Try asking things like:\n"
            "- *Summarize this paper's methodology*\n"
            "- *Compare both papers and suggest future improvements*\n"
            "- *What research gaps exist here?*"
        )

    user_query = st.chat_input("Ask anything about your uploaded research papers...")
    analyze_button = user_query is not None

    return user_query, analyze_button