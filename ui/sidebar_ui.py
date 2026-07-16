# ==========================================================
# SIDEBAR
# Renders the left navigation sidebar: logo, page-switch
# buttons (writes to st.session_state.current_page), and
# the 4 agent-capability preview cards at the bottom.
# ==========================================================

import streamlit as st

def show_sidebar():

    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
        <div style="font-size:30px;">🤖</div>
        <div>
            <div style="font-size:23px;font-weight:700;color:#111827;">ResearchMate</div>
            <div style="font-size:13px;color:#6B7280;">Multi-Agent AI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<p style='font-size:12px;font-weight:700;color:#6B7280;letter-spacing:0.5px;'>NAVIGATION</p>", unsafe_allow_html=True)

    current = st.session_state.get("current_page", "Coordinator")

    nav_items = [
        ("Coordinator", "🏠 Coordinator Agent"),
        ("Analysis", "📄 Analysis Agent"),
        ("QA", "🔎 Research Q&A Agent"),
        ("Comparison", "📊 Comparison Agent"),
        ("Innovation", "💡 Innovation Agent"),
    ]

    for key, label in nav_items:
        is_active = current == key
        if st.button(
            label,
            use_container_width=True,
            type="primary" if is_active else "secondary",
            key=f"nav_{key}"
        ):
            st.session_state.current_page = key

    st.divider()
    st.markdown("<p style='font-size:12px;font-weight:700;color:#6B7280;letter-spacing:0.5px;'>AGENT CAPABILITIES</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.success("📄 **Analysis**\n\nStructured paper summaries.")
        st.success("🔎 **Research Q&A**\n\nAsk cross-paper questions.")
    with col2:
        st.success("📊 **Comparison**\n\nCompare papers instantly.")
        st.success("💡 **Innovation**\n\nFind research gaps.")

    st.divider()
    st.caption("Powered by Multi-Agent AI • Version 1.0")