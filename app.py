import streamlit as st

# 1. SET PAGE CONFIG
st.set_page_config(
    page_title="Scentara Premium",
    page_icon="💎",
    layout="centered"
)

# 2. CSS STYLE (DIPISAH AGAR AMAN)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #020010 0%, #080C1F 50%, #111827 100%);
        color: #FFFFFF;
        font-family: 'Lato', sans-serif;
    }
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        color: #FF4B6E; 
        text-align: center;
        text-shadow: 0px 0px 20px rgba(255, 75, 110, 0.5);
    }
    .result-card {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    h3 { color: #FF8BA7 !important; }
    strong { color: #FFD700; }
</style>
""", unsafe_allow_html=True)

# 3. DATABASE (STRUKTUR FLAT AGAR TIDAK ERROR)
db = {
    "🥩 Daging Merah (Sate/Steak)": {
        "m": "Protein tinggi meningkatkan suhu tubuh (Thermogenesis).",
        "l": "Butuh aroma Spicy & Wood agar tidak kalah dengan bau tubuh.",
        "r": "Oud, Pepper, Leather.",
        "a": "Vanilla manis (bikin mual).",
        "cat": "bold"
    },
    "🧄 Bawang & Rempah (Kari/Sambal)": {
        "m": "Sulfur bawang keluar lewat pori-pori selama 24 jam.",
        "l": "Gunakan Citrus tajam untuk 'memotong' aroma sulfur.",
        "r": "Bergamot, Lemon, Mint.",
        "a": "Bunga Melati/Mawar (indolic).",
        "cat": "fresh"
    },
    "🐟 Seafood (Ikan Bakar/Sushi)": {
        "m": "Zat Trimethylamine menyebabkan aroma amis di kulit.",
        "l": "Gunakan wangi Laut/Aquatic sebagai penetral alami.",
        "r": "Sea Salt, Lime, Sage.",
        "a": "Musk hewani (bikin apek).",
        "cat": "fresh"
    },
    "☕ Kopi & Alkohol": {
        "m": "Efek dehidrasi membuat kulit kering dan parfum cepat hilang.",
        "l": "Gunakan wangi manis (Gourmand) yang punya daya rekat kuat.",
        "r": "Coffee, Vanilla, Tonka Bean.",
        "a": "Cologne ringan (cepat uap).",
        "cat": "sweet"
    },
    "🥗 Sayur & Vegan (Salad)": {
        "m": "Tubuh lebih bersih dan netral. Kanvas terbaik.",
        "l": "Gunakan wangi Clean/Floral untuk kesan elegan.",
        "r": "White Musk, Jasmine, Pear.",
        "a": "Tidak ada pantangan.",
        "cat": "clean"
    }
}

# 4. TAMPILAN
st.markdown('<h1 class="main-header">SCENTARA</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#9CA3AF;">The Scent Sommelier Premium</p>', unsafe_allow_html=True)

menu = st.selectbox("Apa yang Anda makan hari ini?", ["-- Pilih --"] + list(db.keys()))

if menu != "-- Pilih --":
    data = db[menu]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="result-card"><h3>🔬 Analisa</h3><p>{data["m"]}</p><p><b>Logika:</b> {data["l"]}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="result-card"><h3>✅ Rekomendasi</h3><p><strong>Notes:</strong> {data["r"]}</p><p><strong>Hindari:</strong> {data["a"]}</p></div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("🛍️ Rekomendasi Produk (< 200rb)")
    
    # LOGIKA PRODUK
    c = data["cat"]
    if c == "bold":
        p1, l1 = "Kahf Revered Oud", "https://shopee.co.id/search?keyword=kahf%20revered%20oud"
        p2, l2 = "Saff & Co S.O.T.B", "https://shopee.co.id/search?keyword=saff%20and%20co%20sotb"
    elif c == "fresh":
        p1, l1 = "Onix Mexicola", "https://shopee.co.id/search?keyword=onix%20mexicola"
        p2, l2 = "Kahf Humbling Forest", "https://shopee.co.id/search?keyword=kahf%20humbling%20forest"
    elif c == "sweet":
        p1, l1 = "Mykonos Vanilla Clouds", "https://shopee.co.id/search?keyword=mykonos%20vanilla%20clouds"
        p2, l2 = "HMNS Orgsm", "https://shopee.co.id/search?keyword=hmns%20orgsm"
    else:
        p1, l1 = "Lilith & Eve Daisy", "https://shopee.co.id/search?keyword=lilith%20and%20eve%20daisy"
        p2, l2 = "Miniso Garden of Mirror", "https://shopee.co.id/search?keyword=miniso%20garden%20of%20mirror"

    cp1, cp2 = st.columns(2)
    with cp1:
        st.markdown(f'<div class="result-card" style="text-align:center;"><h4>{p1}</h4></div>', unsafe_allow_html=True)
        st.link_button(f"Cek {p1}", l1)
    with cp2:
        st.markdown(f'<div class="result-card" style="text-align:center;"><h4>{p2}</h4></div>', unsafe_allow_html=True)
        st.link_button(f"Cek {p2}", l2)

else:
    st.info("Silakan pilih menu makanan untuk memulai.")
