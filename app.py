import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Scentara Premium - The Scent Sommelier",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
#  CUSTOM CSS: DEEP MIDNIGHT & HIGH CONTRAST
# ==========================================
st.markdown("""
    <style>
    /* IMPORT FONT MEWAH */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Lato:wght@300;400;700&display=swap');

    /* 1. BACKGROUND GRADASI DEEP (Agar teks putih terbaca jelas) */
    .stApp {
        background: linear-gradient(180deg, #020010 0%, #080C1F 50%, #111827 100%);
        color: #FFFFFF;
        font-family: 'Lato', sans-serif;
    }
    
    /* 2. HEADER STYLE */
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        color: #FF4B6E; 
        text-align: center;
        font-weight: 700;
        text-shadow: 0px 0px 25px rgba(255, 75, 110, 0.5);
        margin-top: 10px;
    }
    .sub-header {
        font-size: 1.1rem;
        text-align: center;
        color: #9CA3AF;
        letter-spacing: 3px;
        margin-bottom: 2.5rem;
        text-transform: uppercase;
        font-weight: 300;
    }

    /* 3. INPUT BOX STYLING */
    .stSelectbox > div > div {
        background-color: rgba(20, 20, 30, 0.8) !important;
        border: 1px solid #FF4B6E;
        color: white !important;
        border-radius: 8px;
    }
    /* Warna teks dropdown item */
    div[data-baseweb="select"] ul {
        background-color: #0F172A !important;
        color: white !important;
    }

    /* 4. RESULT CARDS (BASE HITAM TRANSPARAN) */
    .result-card {
        background: rgba(0, 0, 0, 0.6); /* Lebih gelap agar teks pop */
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }
    
    /* 5. TYPOGRAPHY DALAM CARD */
    h3 { color: #FF8BA7 !important; font-family: 'Playfair Display', serif; margin-bottom: 15px; }
    h4 { color: #E5E7EB !important; font-weight: 700; margin-top: 10px; }
    p, li { line-height: 1.7; color: #D1D5DB; font-size: 1rem; }
    strong { color: #FFD700; font-weight: 700; } 

    /* 6. BUTTON CUSTOM */
    .stButton>button {
        background: linear-gradient(90deg, #D61C4E 0%, #990033 100%);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(214, 28, 78, 0.5);
    }
    
    /* 7. TAB STYLE */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.05);
        border-radius: 5px;
        color: #9CA3AF;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(214, 28, 78, 0.2);
        color: #FFFFFF;
        border: 1px solid #D61C4E;
    }
    
    /* DISCLAIMER */
    .disclaimer {
        font-size: 0.75rem;
        color: #6B7280;
        text-align:
