import streamlit as st

# --- KONFIGURASI HALAMAN (PREMIUM TIER) ---
st.set_page_config(
    page_title="Scentara Premium - The Scent Sommelier",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
#  CUSTOM CSS: HIGH CONTRAST LUXURY
# ==========================================
st.markdown("""
    <style>
    /* IMPORT FONT MEWAH */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Lato:wght@300;400;700&display=swap');

    /* 1. BACKGROUND GRADASI LEBIH PEKAT (AGAR TEKS JELAS) */
    .stApp {
        /* Gradasi dari Hitam Navy ke Deep Purple - Kontras tinggi untuk teks putih */
        background: linear-gradient(180deg, #050505 0%, #0B1021 50%, #1B1430 100%);
        color: #FFFFFF; /* Mengubah dari abu-abu (#E0E0E0) ke Putih Murni */
        font-family: 'Lato', sans-serif;
    }
    
    /* 2. HEADER STYLE */
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        color: #FF4B6E; /* Warna sedikit lebih terang dari sebelumnya agar pop */
        text-align: center;
        font-weight: 700;
        text-shadow: 0px 0px 25px rgba(255, 75, 110, 0.6);
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        text-align: center;
        color: #D1D5DB; /* Abu-abu terang */
        letter-spacing: 2px;
        margin-bottom: 3rem;
        text-transform: uppercase;
    }

    /* 3. INPUT BOX STYLING */
    .stSelectbox > div > div {
        background-color: rgba(0, 0, 0, 0.5) !important; /* Background input lebih gelap */
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white !important;
        border-radius: 8px;
    }

    /* 4. RESULT CARDS (PERBAIKAN UTAMA DISINI) */
    .result-card {
        /* UBAH DARI BASIS PUTIH KE BASIS HITAM TRANSPARAN */
        /* Ini membuat teks putih di dalamnya jauh lebih mudah dibaca */
        background: rgba(0, 0, 0, 0.4); 
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.15); /* Border sedikit dipertegas */
        padding: 25px; /* Padding ditambah sedikit */
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    
    /* 5. TYPOGRAPHY DALAM CARD */
    h3 { color: #FF6B88 !important; font-family: 'Playfair Display', serif; text-shadow: 0px 0px 10px rgba(0,0,0,0.5); }
    h4 { color: #F3F4F6 !important; margin-top: 10px; font-weight: 700; }
    p, li { line-height: 1.6; font-size: 1.05rem; } /* Jarak baris diperlebar agar enak dibaca */
    strong { color: #FFD700; font-weight: 700; } 

    /* 6. BUTTON CUSTOM */
    .stButton>button {
        background: linear-gradient(90deg, #E94560 0%, #C81D48 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: 0.3s;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(233, 69, 96, 0.8);
    }
    
    /* 7. TAB STYLE (Agar tulisan di Tab juga jelas) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(0,0,0,0.3);
        border-radius: 5px;
        color: #FFFFFF;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(233, 69, 96, 0.2);
        border-bottom: 2px solid #E94560;
    }
    
    /* DISCLAIMER */
    .disclaimer {
        font-size: 0.8rem;
        color: #9CA3AF;
        text-align: center;
        margin-top: 50px;
        border-top: 1px solid #374151;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)
# --- DATABASE INTELEGENSIA AROMA (EXPANDED & FACTUAL) ---
# Format Data:
# - mechanism: Penjelasan ilmiah (Biologi/Kimia)
# - pairing_logic: Mengapa notes tertentu dipilih
# - recommended_notes: Notes spesifik
# - avoid_notes: Notes yang dilarang & alasannya
# - ritual: Tips detail sebelum/sesudah pakai parfum

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
        "ritual": "Gunakan deodoran *antiperspirant* (bukan hanya deodoran) di malam hari sebelumnya. Semprot parfum di baju (fabric) lebih banyak daripada di kulit langsung."
    },

    "🧄 Bawang & Rempah Tajam (Sambal/Gulai/Kari)": {
        "mechanism": """
        **Senyawa Sulfur (Belerang):** Bawang putih/merah mengandung *Allicin* yang dipecah tubuh menjadi *Allyl Methyl Sulfide (AMS)*. 
        Senyawa ini TIDAK bisa dicerna total, melainkan dikeluarkan lewat darah -> paru-paru (napas) & pori-pori kulit selama 24 jam.
        """,
        "pairing_logic": "Lawan 'panas' dengan 'dingin' atau potong bau sulfur dengan ketajaman sitrus (Citrus cuts through fat and sulfur).",
        "recommended_notes": """
        * **Top Notes:** Bergamot, Grapefruit, Lemon, Mint, Eucalyptus.
        * **Heart/Base:** Vetiver (Akar Wangi), Cedarwood.
        * **Genre:** *Citrus Aromatic* atau *Fougere*.
        """,
        "avoid_notes": "❌ **Heavy Rose & Tuberose:** Bunga yang baunya 'indolic' (sedikit kotor/hewani) akan memperparah bau sulfur dari bawang. Hindari juga *Oud* murah.",
        "ritual": "Minum air lemon hangat. Jangan gosok parfum di pergelangan tangan (gesekan memecah molekul top notes yang bertugas melawan bau bawang)."
    },

    "🐟 Seafood & Terasi (Ikan Bakar/Seafood Saus Padang)": {
        "mechanism": """
        **Trimethylamine:** Senyawa alami pada hasil laut yang memberikan aroma 'amis'. 
        Saat bercampur dengan bakteri kulit, ia menghasilkan aroma amonia tipis. Tubuh juga cenderung memproduksi minyak berlebih jika seafood digoreng.
        """,
        "pairing_logic": "Gunakan prinsip kuliner: Ikan diberi jeruk nipis untuk hilang amisnya. Prinsip ini berlaku sama di parfum.",
        "recommended_notes": """
        * **Top Notes:** Neroli, Lime, Sea Salt, Mandarin Orange.
        * **Heart/Base:** Sage, Ambergris (Notes laut sintetis).
        * **Genre:** *Aquatic* atau *Citrus Marine*.
        """,
        "avoid_notes": "❌ **Musk & Animalic:** Musk bereaksi dengan residu protein laut menjadi aroma yang 'kotor' dan apek.",
        "ritual": "Cuci area leher dengan sabun wajah sebelum re-spray parfum. Pastikan tangan steril dari bau amis sebelum menyentuh botol parfum."
    },

    "☕ Kopi & Alkohol (Kafein Tinggi/Cocktail)": {
        "mechanism": """
        **Dehidrasi & Asiditas:** Alkohol dan kafein bersifat diuretik (membuang cairan), membuat mulut kering (halitosis) dan kulit kering. 
        Kulit kering tidak bisa menahan wangi parfum lama-lama (poor longevity).
        """,
        "pairing_logic": "Karena kulit kering, Anda butuh parfum konsentrasi tinggi (Extrait/EDP) dengan base notes yang lengket (resinous).",
        "recommended_notes": """
        * **Top Notes:** Coffee, Dark Chocolate, Rum.
        * **Heart/Base:** Vanilla, Tonka Bean, Tobacco.
        * **Genre:** *Gourmand* atau *Boozy*.
        """,
        "avoid_notes": "❌ **Light Citrus/Eau de Cologne:** Akan menguap dalam hitungan menit karena kulit tidak punya kelembapan untuk mengikatnya.",
        "ritual": "Wajib pakai *Unscented Body Lotion* atau *Petroleum Jelly* di titik nadi sebelum semprot parfum untuk mengunci wangi."
    },

    "🥦 Sayuran, Buah & Vegan (Gado-gado/Salad)": {
        "mechanism": """
        **Detoksifikasi Alami:** Klorofil dan serat membantu membersihkan racun tubuh. pH tubuh cenderung seimbang dan keringat tidak berbau tajam. 
        Ini adalah 'kanvas bersih' untuk parfum.
        """,
        "pairing_logic": "Tubuh Anda netral. Ini saatnya memakai parfum yang *complex* atau *delicate* yang biasanya kalah jika dipakai saat berkeringat.",
        "recommended_notes": """
        * **Bebas Eksplorasi:** White Floral (Jasmine/Gardenia), Fruity, atau Skin Scents (Iso E Super).
        * **Genre:** *Floral Aldehyde* atau *Musky*.
        """,
        "avoid_notes": "❌ **Tidak Ada:** Hampir semua jenis parfum akan tercium *true-to-scent* (sesuai aslinya) di kulit Anda.",
        "ritual": "Semprotkan di belakang lutut dan siku bagian dalam untuk *sillage* (jejak wangi) yang sopan namun elegan."
    },
    
    "🍝 Karbohidrat Olahan & MSG (Mie Instan/Fast Food)": {
        "mechanism": """
        **Glicemic Spike & Oily Skin:** Lonjakan gula darah dan kandungan minyak jenuh memicu produksi sebum (minyak wajah/kulit). 
        Parfum pada kulit berminyak bertahan lebih lama tapi *top notes*-nya bisa berubah menjadi apek jika oksidasi.
        """,
        "pairing_logic": "Anda butuh wangi yang 'Clean', 'Soapy', atau 'Powdery' untuk menetralkan kesan berminyak dan lengket.",
        "recommended_notes": """
        * **Top Notes:** Aldehydes (Wangi sabun), White Musk, Iris.
        * **Heart/Base:** Cotton flower, Lily of the Valley.
        * **Genre:** *Clean Laundry* atau *Powdery Floral*.
        """,
        "avoid_notes": "❌ **Heavy Spices (Cengkeh/Kayu Manis):** Akan membuat kesan tubuh semakin 'panas' dan tidak segar.",
        "ritual": "Sedia *blooting paper* (kertas minyak) untuk wajah. Parfum tipe *Clean* sangat disarankan disemprot ulang tiap 4-5 jam."
    }
}

# --- HEADER ---
st.markdown('<div class="main-header">SCENTARA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Premium Personal Scent Consultant</div>', unsafe_allow_html=True)

# --- INPUT SECTION ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_menu = st.selectbox(
        "Apa dominasi makanan Anda hari ini?",
        ["-- Pilih Menu --"] + list(database_premium.keys())
    )

# --- LOGIKA UTAMA & TAMPILAN ---
if selected_menu and selected_menu != "-- Pilih Menu --":
    data = database_premium[selected_menu]
    
    st.markdown("---")
    
    # MENGGUNAKAN TABS UNTUK UI YANG LEBIH RAPI & INTERAKTIF
    tab1, tab2, tab3 = st.tabs(["🔬 Analisa Molekuler", "💎 Rekomendasi Parfum", "✨ Ritual Pemakaian"])
    
    with tab1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### 🧬 Bagaimana Tubuh Bereaksi?")
        st.info(data['mechanism'])
        st.markdown(f"**Strategi Aroma:** {data['pairing_logic']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        col_rec, col_avoid = st.columns(2)
        
        with col_rec:
            st.markdown("### ✅ Harmony Match")
            st.success(data['recommended_notes'])
            
        with col_avoid:
            st.markdown("### ⛔ Clashing Notes")
            st.error(data['avoid_notes'])
            
        st.markdown("#### 💡 Scentara Pro Tip:")
        st.markdown("Jika Anda tidak memiliki parfum dengan notes spesifik di atas, carilah parfum dengan label warna botol yang senada (Misal: Citrus biasanya botol kuning/hijau muda, Woody botol cokelat/hitam).")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### 🧖 Ritual Aplikasi (Longevity Hack)")
        st.warning(data['ritual'])
        st.markdown("""
        **Panduan Titik Semprot:**
        1.  **Nadi Leher:** Untuk *projection* (agar orang lain mencium).
        2.  **Belakang Telinga:** Agar wangi bertahan saat berpelukan/cipika-cipiki.
        3.  **Baju (Bahu):** Agar wangi tidak bereaksi dengan kimia keringat (Safe zone).
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION AFFILIATE YANG LEBIH ELEGANT ---
    st.markdown("---")
    st.subheader("🛍️ Curated Collections for You")
    st.write("Berdasarkan analisa profil aroma Anda hari ini, berikut adalah rekomendasi produk lokal terbaik yang telah kami kurasi:")
    
    c1, c2, c3 = st.columns(3)
    
    # Logika Tampilan Produk (Bisa disesuaikan linknya)
    if "Daging" in selected_menu or "Rempah" in selected_menu:
        with c1:
            st.image("https://down-id.img.susercontent.com/file/id-11134207-7r98o-lty68p0h4z6f13", caption="Saff & Co - SOTB (Spicy & Bold)")
            st.link_button("Lihat Produk", "https://shopee.co.id/Saff-Co-Extrait-de-Parfum-SOTB-30ml-i.294337637.3168246473")
        with c2:
            st.image("https://down-id.img.susercontent.com/file/id-11134207-7r98r-lsm5h4k8k8j790", caption="HMNS - Alpha (Green Tea & Woody)")
            st.link_button("Lihat Produk", "https://shopee.co.id/HMNS-Perfume-Alpha-100ml-i.168973347.2628434774")
    elif "Seafood" in selected_menu or "MSG" in selected_menu:
         with c1:
            st.image("https://down-id.img.susercontent.com/file/id-11134207-7qul6-lfz5r5x5q3b266", caption="Onix - Mexicola (Fresh Citrus)")
            st.link_button("Lihat Produk", "https://shopee.co.id/Onix-Parfum-Mexicola-50ml-i.273663363.6338576402")
    else:
         with c1:
            st.image("https://down-id.img.susercontent.com/file/sg-11134201-22100-24y444y444jv40", caption="Lilith & Eve - Daisy (Clean Floral)")
            st.link_button("Lihat Produk", "https://shopee.co.id/Lilith-Eve-Daisy-Eau-De-Parfum-i.679237666.14364234024")

    st.info("ℹ️ *Produk di atas adalah rekomendasi Official Store yang terjamin keasliannya.*")

else:
    # TAMPILAN AWAL SEBELUM MEMILIH
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 40px; background: rgba(255,255,255,0.05); border-radius: 10px;">
        <h3>👋 Selamat Datang di Scentara Premium</h3>
        <p>Aplikasi ini menggunakan pendekatan kimiawi untuk menyelaraskan aroma parfum dengan metabolisme tubuh Anda setelah makan.</p>
        <p>Silakan pilih menu makanan Anda di atas untuk memulai konsultasi.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="disclaimer">
        <b>Scentara Premium v3.1</b><br>
        All rights reserved. Data based on perfume chemistry principles & dermatology research.<br>
        <i>Disclaimer: Hasil reaksi bisa berbeda tergantung genetika dan kondisi hormon individu.</i>
    </div>
""", unsafe_allow_html=True)
