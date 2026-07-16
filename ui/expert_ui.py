# ==========================================================
# EXPERT PAGE HEADER
# Renders the colored banner + result container used by
# EVERY individual agent page (Analysis/QA/Comparison/
# Innovation). AGENT_STYLES maps each agent's title to its
# accent color so each agent has a consistent visual identity.
# ==========================================================

import streamlit as st

AGENT_STYLES = {
    "📄 Research Analysis Agent": ("#2563EB", "#EFF6FF"),
    "🔎 Research Q&A Agent": ("#7C3AED", "#F5F3FF"),
    "📊 Comparative Intelligence Agent": ("#EA580C", "#FFF7ED"),
    "💡 Research Innovation Agent": ("#059669", "#ECFDF5"),
}

def show_expert_page(title):
    accent, bg = AGENT_STYLES.get(title, ("#2563EB", "#EFF6FF"))

    st.markdown(f"""
    <div style="
        border-left: 4px solid {accent};
        background: {bg};
        padding: 14px 18px;
        border-radius: 10px;
        margin: 24px 0 12px 0;
    ">
        <span style="font-size:22px;font-weight:700;color:#111827;">{title}</span>
    </div>
    """, unsafe_allow_html=True)

    result_container = st.container(border=True)

    return result_container