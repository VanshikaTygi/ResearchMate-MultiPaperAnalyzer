import streamlit as st

def show_home_header():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 55%, #38BDF8 100%);
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 24px;
        color: white;
    ">
        <div style="font-size:42px;font-weight:800;margin-bottom:6px;">📚 ResearchMate AI</div>
        <div style="font-size:18px;opacity:0.95;margin-bottom:14px;">Multi-Agent Research Intelligence Platform</div>
        <div style="font-size:14px;opacity:0.88;margin-bottom:16px;">Analyze • Compare • Ask Questions • Discover Research Gaps</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:rgba(255,255,255,0.2);padding:6px 13px;border-radius:20px;font-size:13px;font-weight:600;">🔗 LangChain</span>
            <span style="background:rgba(255,255,255,0.2);padding:6px 13px;border-radius:20px;font-size:13px;font-weight:600;">🧠 FAISS Vector DB</span>
            <span style="background:rgba(255,255,255,0.2);padding:6px 13px;border-radius:20px;font-size:13px;font-weight:600;">⚡ Groq LLM</span>
            <span style="background:rgba(255,255,255,0.2);padding:6px 13px;border-radius:20px;font-size:13px;font-weight:600;">🎈 Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)