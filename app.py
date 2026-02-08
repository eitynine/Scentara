import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Scentara - Personal Scent Guide",
    page_icon="👃",
    layout="centered"
)

# ==========================================
#  CUSTOM CSS BACKGROUND & STYLE PREMIUM
# ==========================================
st.markdown("""
    <style>
    /* 1. BACKGROUND UTAMA GRADASI */
    .stApp {
        background: linear-gradient(135deg, #FF9966 0%, #FF5E62 100%); /* Gradasi Oranye-Merah Hangat */
        background-attachment: fixed; /* Agar background tidak ikut scroll */
    }
    
    /* 2. MEMPERCANTIK KOTAK INPUT */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.8) !important; /* Putih transparan */
        border-radius: 10px !important;
        color: #333 !important;
    }
    .stSelectbox label {
        color: white !important; /* Warna label input jadi putih */
        font-weight: bold;
    }

    /* 3. STYLE EFEK KACA UNTUK SEMUA BOX INFORMASI (Glassmorphism) */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.85) !important; /* Efek kaca transparan */
        backdrop-filter: blur(10px); /* Efek blur di belakang box */
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #2c3e50 !important; /* Warna teks di dalam box jadi gelap agar terbaca */
    }
    /* Khusus box Sukses (Hijau) */
    .stAlert[data-testid="stAlertSuccess"] { border-left: 5px solid #2ecc71 !important; }
    /* Khusus box Error (Merah) */
    .stAlert[data-testid="stAlertError"] { border-left: 5px solid #e74c3c !important; }
    /* Khusus box Info (Biru) */
    .stAlert[data-testid="stAlertInfo"] { border-left: 5px solid #3498db !important; }
    /* Khusus box Warning (Kuning) */
    .stAlert[data-testid="stAlertWarning"] { border-left: 5px solid #f1c40f !important; }

    /* 4. STYLE HEADER YANG LEBIH MENONJOL */
    .main-header {
        font-size: 3.5rem;
        color: #FFFFFF; /* Warna teks putih */
        text-align: center;
        font-weight: 800;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Bayangan agar teks pop-out */
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #F0F0F0; /* Putih gading */
        margin-bottom: 3rem;
    }

    /* 5. STYLE DISCLAIMER BOX KHUSUS */
    .disclaimer-box {
        background-color: rgba(255, 235, 238, 0.9); /* Merah muda transparan */
        padding: 15px;
        border: 2px solid #ffcccb;
        border-radius: 10px;
        font-size: 0.9rem;
        color: #c0392b;
        margin-top: 30px;
        text-align: center;
    }
    
    /* 6. STYLE CAPTION FOOTER */
    .stCaption {
        color: rgba(255,255,255,0.7) !important;
        text-align: center;
    }
    
    /* 7. JUDUL HASIL ANALISA */
    h3 {
        color: white !important;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Garis pemisah (Divider) jadi putih transparan */
    hr { border-color: rgba(255,255,255,0.4) !important; }

    </style>
""", unsafe_allow_html=True)
# ==========================================
# AKHIR STYLE CUSTOM
# ==========================================


# --- HEADER APLIKASI ---
st.markdown('<div class="main-header">✨ Scentara</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Harmonisasi Aroma Tubuh & Kuliner Nusantara</div>', unsafe_allow_html=True)

# --- DATABASE LOGIKA (SAMA SEPERTI SEBELUMNYA - TIDAK BERUBAH) ---
database_aroma = {
    "--- PILIH KATEGORI MAKANAN ---": None,

    # --- KATEGORI KHUSUS: PENGHILANG BAU (HALODOC) ---
    "✨ [PENETRAL] Yoghurt & Susu (Probiotik)": {
        "efek": "🍃 **Pembersih Alami:** Kandungan bakteri baik membantu mengurangi senyawa kolin dalam tubuh yang menyebabkan bau amis/tengik.",
        "cocok": "🌸 **Floral Manis atau Soft Musk:** Kulit dalam kondisi bersih secara internal, wangi lembut akan terpancar sempurna.",
        "larangan": "Tidak ada pantangan khusus. Parfum favoritmu akan tercium lebih 'true to scent'.",
        "tips": "Konsumsi rutin untuk memperbaiki aroma alami tubuh jangka panjang."
    },
    "✨ [PENETRAL] Jeruk / Lemon / Buah Sitrus": {
        "efek": "🍋 **Anti-Oksidan:** Asam sitrat membantu detoksifikasi racun yang keluar lewat pori-pori.",
        "cocok": "🍃 **Fresh Aromatic atau Tea-based scents:** Menambah kesan segar dan energik.",
        "larangan": "Parfum yang terlalu 'Oud' atau berat mungkin terasa terlalu kontras dengan kesegaran tubuhmu.",
        "tips": "Minum air lemon hangat setiap pagi sangat membantu detoks aroma tubuh."
    },
    "✨ [PENETRAL] Green Tea (Teh Hijau)": {
        "efek": "🍵 **Polifenol:** Menangkal bakteri penyebab bau badan langsung dari dalam sistem metabolisme.",
        "cocok": "🌬️ **Aquatic atau Ozonic:** Memberikan kesan 'bersih' seperti baru selesai mandi.",
        "larangan": "Hampir tidak ada.",
        "tips": "Pilihan terbaik jika kamu ingin tampil dengan 'Clean Girl/Boy Aesthetic'."
    },

    # --- MAKANAN SUMATERA ---
    "🍛 [SUMATERA] Rendang, Mie Aceh, Gulai Malbi": {
        "efek": "🔥 **Rempah Sangat Kuat:** Campuran lada, kapulaga, dan santan kental membuat keringat lebih tajam dan berminyak.",
        "cocok": "🪵 **Woody, Amber, atau Tobacco:** Notes berat ini 'merangkul' aroma rempah tubuh menjadi kesan eksotis.",
        "larangan": "Citrus tipis (akan bau kecut) atau Floral murni (jadi apek).",
        "tips": "Fokus semprot parfum di titik nadi yang jauh dari area berkeringat banyak."
    },
    "🐟 [SUMATERA] Pempek, Tempoyak, Arsik Ikan": {
        "efek": "🦐 **Asam & Amis:** Cuka (Cuko) dan fermentasi ikan/durian meninggalkan jejak aroma asam yang persisten.",
        "cocok": "🍊 **Citrus Sharp (Bergamot/Neroli):** Aroma jeruk tajam sangat efektif memotong bau amis.",
        "larangan": "Vanilla atau Caramel (perpaduan asam cuka + manis bisa bikin mual).",
        "tips": "Gunakan sabun cuci tangan anti-amis sebelum memegang area leher."
    },

    # --- MAKANAN JAWA ---
    "🥘 [JAWA] Rawon, Gudeg, Selat Solo": {
        "efek": "🟤 **Earthy & Sweet:** Kluwak (Rawon) memberikan efek 'earthy' pada keringat, sementara Gudeg cenderung netral namun manis.",
        "cocok": "🍂 **Patchouli atau Sandalwood:** Menambah kesan elegan dan menyatu dengan aroma alami kulit yang hangat.",
        "larangan": "Parfum aroma Permen (Candy) yang terlalu sintetis.",
        "tips": "Rawon memiliki aroma kuat, pastikan sirkulasi udara baik saat makan agar bau tidak menempel di baju."
    },
    "🍜 [JAWA] Bakso, Mie Ayam, Soto Lamongan": {
        "efek": "🧅 **Bawang Goreng & Seledri:** Residu bawang putih dalam kuah bisa tercium samar lewat pori-pori.",
        "cocok": "🧼 **Clean Laundry atau Soap-like scents:** Menetralkan kesan 'oily' setelah makan mie kuah.",
        "larangan": "Parfum rempah berat (Spicy).",
        "tips": "Lap keringat di area wajah/leher segera setelah makan kuah panas."
    },

    # --- MAKANAN BALI, NTB, NTT ---
    "🌶️ [BALI/NUSA] Ayam Betutu, Plecing Kangkung, Se'i Sapi": {
        "efek": "🌋 **Pedas Panas & Asap:** Base genep (Bali) dan aroma asap (Se'i) sangat dominan meresap ke dalam pori-pori.",
        "cocok": "🔥 **Incense, Vetiver, atau Spices:** Jika tubuhmu beraroma asap, parfum smoky justru akan tercium sangat maskulin/karismatik.",
        "larangan": "Aquatic yang terlalu 'berair'.",
        "tips": "Gunakan body mist yang segar di baju, tapi parfum woody di kulit."
    },

    # --- MAKANAN KALIMANTAN & SULAWESI ---
    "🥥 [KAL/SUL] Soto Banjar, Coto Makassar, Konro": {
        "efek": "🥜 **Nutty & Savory:** Kandungan kacang dan kayu manis dalam bumbu membuat aroma tubuh terasa 'gurih'.",
        "cocok": "🍦 **Gourmand (Semi-sweet) atau Spicy Amber:** Menciptakan aura yang hangat dan ramah.",
        "larangan": "Floral Rose yang terlalu kewanitaan.",
        "tips": "Aroma Coto sangat kuat, disarankan menyemprot parfum *setelah* selesai makan."
    },

    # --- MAKANAN PAPUA & MALUKU ---
    "🥣 [PAPUA/MALUKU] Papeda, Ikan Kuah Kuning": {
        "efek": "🍋 **Acidic & Fresh:** Cenderung lebih aman karena minim lemak trans, namun kunyit pada kuah kuning memiliki efek panas.",
        "cocok": "🌿 **Herbal atau White Floral:** Cocok dengan karakter makanan yang segar dari alam.",
        "larangan": "Leather (Kulit) yang terlalu berat.",
        "tips": "Kondisi tubuh cenderung netral, parfum apapun akan bekerja dengan baik."
    }
}

# --- BAGIAN INPUT USER ---
st.markdown("### 🔍 Cek Reaksi Aroma")
selected_food = st.selectbox(
    "Pilih atau cari makanan yang kamu konsumsi hari ini:",
    list(database_aroma.keys())
)

# --- BAGIAN LOGIKA & OUTPUT ---
if selected_food and selected_food != "--- PILIH KATEGORI MAKANAN ---":
    data = database_aroma[selected_food]
    
    st.divider()
    st.subheader(f"Hasil Analisa: {selected_food}")
    
    # Kotak-kotak ini sekarang punya efek transparan (Glassmorphism)
    st.info(data["efek"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"✅ **COCOK:**\n\n{data['cocok']}")
    with col2:
        st.error(f"❌ **HINDARI:**\n\n{data['larangan']}")
        
    st.warning(f"💡 **TIPS EXTRA:**\n{data['tips']}")

# --- DISCLAIMER (Sesuai Permintaan) ---
st.markdown(f"""
    <div class="disclaimer-box">
        <b>PENTING:</b> Aplikasi <b>Scentara</b> dibuat semata-mata sebagai panduan gaya hidup untuk mengecek potensi perubahan aroma badan akibat reaksi kimia makanan. 
        Aplikasi ini <b>SAMA SEKALI TIDAK</b> bermaksud melarang pengguna untuk mengonsumsi makanan yang disukai. 
        Kekayaan kuliner Nusantara adalah warisan yang patut dinikmati; kami hanya membantu Anda tetap tampil wangi setelah menikmatinya.
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.caption("Scentara v2.0 (Premium Style) | Data diriset dari berbagai sumber kesehatan dan komunitas pecinta parfum Indonesia.")
