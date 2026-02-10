import streamlit as st

# --- KONFIGURASI HALAMAN (PREMIUM TIER) ---
st.set_page_config(
    page_title="Scentara Premium - The Scent Sommelier",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
#  CUSTOM CSS: LUXURY, READABILITY & CONTRAST FIX
# ==========================================
st.markdown("""
    <style>
    /* IMPORT FONT MEWAH */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Lato:wght@300;400;700&display=swap');

    /* 1. BACKGROUND GRADASI PREMIUM (LEBIH DALAM) */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #FFFFFF; /* Default text putih mutlak */
        font-family: 'Lato', sans-serif;
    }
    
    /* 2. HEADER STYLE */
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        color: #FFD700; /* Emas */
        text-align: center;
        font-weight: 700;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        margin-bottom: 5px;
        padding-top: 20px;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #E0E0E0;
        letter-spacing: 2px;
        margin-bottom: 2.5rem;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255,215,0,0.3);
        padding-bottom: 20px;
    }

    /* 3. INPUT BOX & LABEL FIX (Supaya Terlihat Jelas) */
    .stSelectbox label {
        color: #FFD700 !important; /* Label Emas Cerah */
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px black;
    }
    .stSelectbox > div > div {
        background-color: rgba(0, 0, 0, 0.7) !important; /* Background input gelap */
        border: 1px solid #FFD700 !important; /* Border Emas */
        color: white !important;
        border-radius: 8px;
    }
    /* Warna teks dropdown item */
    div[data-baseweb="popover"] {
        background-color: #1a1a1a !important;
    }

    /* 4. TABS STYLING (Supaya Judul Tab Terbaca) */
    button[data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        border-radius: 5px 5px 0 0;
        margin-right: 2px;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #FFD700 !important; /* Tab Aktif jadi Emas */
        color: #000000 !important; /* Teks Hitam supaya kontras */
    }

    /* 5. RESULT CARDS (High Contrast Glassmorphism) */
    .result-card {
        background: rgba(0, 0, 0, 0.75); /* Opacity 75% Gelap - Teks Putih pasti terbaca */
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.3); /* Border Emas Tipis */
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* 6. TYPOGRAPHY DALAM CARD */
    h3 { color: #FFD700 !important; font-family: 'Playfair Display', serif; text-shadow: 1px 1px 2px black; }
    h4 { color: #81D4FA !important; margin-top: 15px; font-weight: bold; } /* Sub-judul biru muda cerah */
    p, li { color: #FFFFFF !important; line-height: 1.6; }
    strong { color: #FFEB3B; } /* Kuning terang untuk penekanan */

    /* 7. DISCLAIMER */
    .disclaimer {
        font-size: 0.8rem;
        color: #B0B0B0;
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background: rgba(0,0,0,0.8);
        border-radius: 10px;
    }
    
    /* 8. LINK BUTTON */
    .stLinkButton > a {
        background: linear-gradient(45deg, #FFD700, #FFC107);
        color: black !important;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        text-align: center;
        display: block;
    }
    .stLinkButton > a:hover {
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE INTELEGENSIA AROMA (LENGKAP) ---
database_premium = {
    "🥩 Daging Merah & Berlemak (Sate Kambing/Rendang/Steak)": {
        "mechanism": """
        **Efek Metabolik:** Mencerna daging merah membutuhkan energi tinggi (Thermogenesis), memicu keringat lebih banyak. 
        Residu asam amino memecah menjadi amonia, mengubah pH kulit menjadi lebih basa (alkali), membuat parfum floral/fruity cepat rusak baunya.
        """,
        "pairing_logic": "Anda membutuhkan notes yang 'berat' dan earthy untuk menyamarkan residu amonia, atau notes rempah untuk menyeimbangkan karakter 'animalic' tubuh.",
        "recommended_notes": """
        * **Top Notes:** Black Pepper, Cardamom (Menyamarkan tajamnya bau keringat).
        * **Heart/Base:** Oud (Gaharu), Leather, Patchouli, atau Sandalwood.
        * **Genre:** *Spicy Amber* atau *Woody Aromatic*.
        """,
        "avoid_notes": "❌ **Sweet Gourmand (Vanilla/Caramel) & Aquatic:** Aroma manis gula akan berbenturan dengan aroma residu lemak, menciptakan efek bau 'tengik' atau mual.",
        "ritual": "Gunakan deodoran *antiperspirant* (bukan hanya deodoran) di malam hari sebelumnya. Semprot parfum di baju (fabric) lebih banyak daripada di kulit langsung.",
        "keyword_shopee": "parfum oud leather pria wanita"
    },

    "🧄 Bawang & Rempah Tajam (Sambal/Gulai/Kari)": {
        "mechanism": """
        **Senyawa Sulfur (Belerang):** Bawang putih/merah mengandung *Allicin* yang dipecah tubuh menjadi *Allyl Methyl Sulfide (AMS)*. 
        Senyawa ini TIDAK bisa dicerna total
