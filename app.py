import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Scentara Premium - The Scent Sommelier",
    page_icon="💎",
    layout="centered"
)

# ==========================================
#  CUSTOM CSS: HIGH CONTRAST & READABILITY
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap');

    /* 1. BACKGROUND LEBIH GELAP UNTUK KONTRAS MAKSIMAL */
    .stApp {
        background: linear-gradient(135deg, #050505 0%, #1a1a2e 100%);
        color: #FFFFFF;
        font-family: 'Lato', sans-serif;
    }
    
    /* 2. JUDUL UTAMA (EMAS TERANG) */
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        color: #FFD700;
        text-align: center;
        text-shadow: 3px 3px 15px rgba(0,0,0,1);
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.3rem;
        text-align: center;
        color: #FFFFFF;
        letter-spacing: 3px;
        margin-bottom: 2rem;
        text-transform: uppercase;
        font-weight: bold;
    }

    /* 3. INPUT SELECTBOX (SANGAT TERLIHAT) */
    .stSelectbox label {
        color: #FFD700 !important;
        font-size: 1.4rem !important;
        background: rgba(0,0,0,0.5);
        padding: 5px 15px;
        border-radius: 5px;
    }
    .stSelectbox > div > div {
        background-color: #FFFFFF !important; /* Putih Solid agar teks menu terbaca */
        color: #000000 !important;
        border: 3px solid #FFD700 !important;
        border-radius: 10px;
    }

    /* 4. TABS (KUNING EMAS) */
    button[data-baseweb="tab"] {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFD700 !important;
        border-bottom-color: #FFD700 !important;
    }

    /* 5. CARD HASIL (HITAM PEKAT AGAR TEKS PUTIH JELAS) */
    .result-card {
        background: rgba(0, 0, 0, 0.85);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    
    h3 { color: #FFD700 !important; }
    p, li { font-size: 1.1rem !important; line-height: 1.7; color: #FFFFFF !important; }

    /* 6. TOMBOL SHOPPING */
    .stLinkButton a {
        background: #FFD700 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        border-radius: 50px !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE ---
# Data diletakkan dalam variabel tunggal untuk menghindari error triple-quote
db = {
    "🥩 Daging Merah & Berlemak": {
        "m": "Mencerna daging merah memicu panas tubuh (Thermogenesis) dan residu amonia yang mengubah pH kulit menjadi basa.",
        "l": "Gunakan notes berat/kayu untuk menyeimbangkan karakter animalic tubuh.",
        "r": "Oud, Leather, Sandalwood, Black Pepper.",
        "a": "Vanilla & Fruity manis (Bisa berbau tengik jika bercampur keringat lemak).",
        "t": "Gunakan lotion tanpa aroma sebelum menyemprot parfum.",
        "kw": "parfum oud sandalwood pria"
    },
    "🧄 Bawang & Rempah Tajam": {
        "m": "Kandungan Allicin keluar lewat pori-pori dan napas selama 24 jam setelah makan.",
        "l": "Potong aroma sulfur dengan ketajaman sitrus yang segar.",
        "r": "Bergamot, Lemon, Mint, Vetiver.",
        "a": "Rose & Tuberose (Aroma bunga berat justru memperparah bau bawang).",
        "t": "Minum air lemon hangat untuk detoksifikasi dari dalam.",
        "kw": "parfum bergamot mint fresh"
    },
    "🐟 Seafood & Terasi": {
        "m": "Residu Trimethylamine menghasilkan aroma amis tipis pada area nadi yang hangat.",
        "l": "Gunakan aroma laut (Marine) untuk menyamarkan sisa aroma amis.",
        "r": "Sea Salt, Neroli, Lime, Sage.",
        "a": "Musk Berat (Bereaksi menjadi bau apek/kotor).",
        "t": "Cuci tangan dan leher dengan sabun antiseptik sebelum semprot.",
        "kw": "parfum sea salt aquatic"
    },
    "☕ Kopi & Alkohol": {
        "m": "Menyebabkan dehidrasi kulit sehingga molekul parfum tidak punya pegangan untuk bertahan lama.",
        "l": "Gunakan parfum dengan konsentrasi Extrait atau EDP yang 'lengket'.",
        "r": "Coffee, Vanilla, Tobacco, Tonka Bean.",
        "a": "Eau de Cologne ringan (Akan hilang dalam 15 menit).",
        "t": "Oleskan vaseline di titik nadi agar wangi terkunci.",
        "kw": "parfum vanilla tobacco"
    }
}

# --- UI LOGIC ---
st.markdown('<div class="main-header">SCENTARA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Premium Personal Scent Guide</div>', unsafe_allow_html=True)

choice = st.selectbox("APA MAKANAN ANDA HARI INI?", list(db.keys()), index=None, placeholder="Pilih menu...")

if choice:
    data = db[choice]
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    
    t1, t2, t3 = st.tabs(["🔬 ANALISA", "💎 REKOMENDASI", "🛍️ BELI"])
    
    with t1:
        st.write(f"### 🧪 Reaksi Tubuh")
        st.write(data['m'])
        st.write(f"**Strategi:** {data['l']}")
        
    with t2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.success(f"**✅ COCOK:**\n\n{data['r']}")
        with col_b:
            st.error(f"**❌ HINDARI:**\n\n{data['a']}")
        st.warning(f"**💡 TIPS:** {data['t']}")
        
    with t3:
        st.write("### 🛒 Rekomendasi Produk")
        st.write("Kami menemukan koleksi yang paling pas untuk kondisi Anda:")
        search_url = f"https://shopee.co.id/search?keyword={data['kw'].replace(' ', '+')}"
        st.link_button(f"Cek Koleksi {choice.split(' ')[1]} di Shopee", search_url)
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Silakan pilih menu di atas untuk melihat analisa aroma.")

st.markdown('<div style="text-align:center; margin-top:50px; opacity:0.5;">Scentara Premium v4.0</div>', unsafe_allow_html=True)
