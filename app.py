import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Scentara Premium - The Scent Sommelier",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
#  CUSTOM CSS: HIGH CONTRAST & LUXURY
# ==========================================
st.markdown("""
    <style>
    /* IMPORT FONT MEWAH */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Lato:wght@300;400;700&display=swap');

    /* 1. BACKGROUND BARU (LEBIH GELAP & KONTRAS) */
    .stApp {
        /* Menggunakan warna dasar Charcoal ke Hitam agar teks Putih terbaca jelas */
        background: linear-gradient(135deg, #121212 0%, #232526 100%);
        color: #F0F0F0;
        font-family: 'Lato', sans-serif;
    }
    
    /* 2. PERBAIKAN LABEL INPUT (Supaya terbaca jelas) */
    .stSelectbox label p {
        font-size: 1.2rem !important;
        color: #FFFFFF !important; /* Warna Putih Mutlak */
        font-weight: 700 !important; /* Tebal */
        text-shadow: 0px 2px 4px rgba(0,0,0,0.8); /* Bayangan agar tidak samar */
    }

    /* 3. HEADER STYLE */
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        color: #D4AF37; /* Ganti ke Emas agar lebih terbaca di background gelap */
        text-align: center;
        font-weight: 700;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.4);
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        text-align: center;
        color: #CCCCCC;
        letter-spacing: 2px;
        margin-bottom: 3rem;
        text-transform: uppercase;
    }

    /* 4. INPUT BOX STYLING */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white !important;
        border-radius: 8px;
    }

    /* 5. RESULT CARDS (GLASSMORPHISM) */
    .result-card {
        background: rgba(30, 30, 30, 0.6); /* Lebih gelap sedikit agar tulisan terbaca */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    
    /* 6. TYPOGRAPHY DALAM CARD */
    h3 { color: #D4AF37 !important; font-family: 'Playfair Display', serif; } /* Gold headers */
    h4 { color: #FFFFFF !important; margin-top: 10px; }
    strong { color: #FFD700; } 

    /* 7. BUTTON CUSTOM */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #C5A028 100%); /* Gold Button */
        color: black;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.6);
        color: white;
    }
    
    /* DISCLAIMER */
    .disclaimer {
        font-size: 0.8rem;
        color: #888;
        text-align: center;
        margin-top: 50px;
        border-top: 1px solid #333;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE INTELEGENSIA AROMA ---
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
    
    # MENGGUNAKAN TABS
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

    # --- SECTION AFFILIATE (UPDATED: < 200rb) ---
    st.markdown("---")
    st.subheader("🛍️ Curated Collections (Under 200K)")
    st.write("Rekomendasi produk lokal & affordable terbaik sesuai profil Anda:")
    
    c1, c2, c3 = st.columns(3)
    
    # LOGIKA PRODUK BARU (HARGA TERJANGKAU & NAMA JELAS)
    if "Daging" in selected_menu or "Rempah" in selected_menu or "Kopi" in selected_menu:
        # Butuh: Woody, Oud, Spicy, Gourmand (Budget Friendly)
        with c1:
            st.image("https://down-tx-id.img.susercontent.com/sg-11134201-7repz-m8pwockowu4xed.webp", caption="Kahf Revered Oud (Oud & Rose)")
            # Harga rata-rata: Rp 70.000 - Rp 80.000
            st.link_button("Cari di Shopee", "https://s.shopee.co.id/8zzdHW7p5O")
        with c2:
            st.image("https://down-tx-id.img.susercontent.com/id-11134207-8224v-mgxa9h3mz0nj34.webp", caption="Saff & Co S.O.T.B (30ml)")
            # Harga rata-rata: Rp 189.000 - Rp 199.000 (Masuk Budget)
            st.link_button("Cari di Shopee", "https://s.shopee.co.id/1LaC9bW5Jv")
            
    elif "Seafood" in selected_menu or "MSG" in selected_menu:
        # Butuh: Citrus, Fresh, Aquatic (Budget Friendly)
        with c1:
             st.image("https://down-tx-id.img.susercontent.com/sg-11134201-821f1-mgn1jjovwkqx8e.webp", caption="Kahf Humbling Forest (Cypress)")
             # Harga rata-rata: Rp 290.000
             st.link_button("Cari di Shopee", "https://s.shopee.co.id/8KjwUbbP0s")
        with c2:
             st.image("https://down-tx-id.img.susercontent.com/id-11134207-7rasa-m2xw4u1vfht9bc.webp", caption="Romano Eau De Parfum Force")
             # Harga rata-rata: Rp 40.000 - Rp 50.000
             st.link_button("Cari di Shopee", "https://s.shopee.co.id/6fbiVeW7W6")

    else:
         # Butuh: Floral, Clean, Musky (Budget Friendly)
         with c1:
            st.image("https://down-tx-id.img.susercontent.com/sg-11134201-23010-o3tc51tgjtlv80.webp", caption="Lilith & Eve Daisy (Floral Fresh)")
            # Harga rata-rata: Rp 78.000
            st.link_button("Cari di Shopee", "https://s.shopee.co.id/9KcTgi9TPB")
         with c2:
            st.image("https://down-tx-id.img.susercontent.com/id-11134207-81zto-mentxgtm0ikn93.webp", caption="Pinkberry Eau De Parfum Wild Berry")
            # Harga rata-rata: Rp 50.000
            st.link_button("Cari di Shopee", "https://s.shopee.co.id/6pv8iCctu5")

    st.info("ℹ️ *Produk dipilih berdasarkan ketersediaan stok lokal dan harga di bawah Rp 200.000.*")

else:
    # TAMPILAN AWAL SEBELUM MEMILIH
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 40px; background: rgba(255,255,255,0.05); border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
        <h3>👋 Selamat Datang di Scentara Premium</h3>
        <p style="color: #ddd;">Aplikasi ini menggunakan pendekatan kimiawi untuk menyelaraskan aroma parfum dengan metabolisme tubuh Anda setelah makan.</p>
        <p style="color: #fff; font-weight: bold;">Silakan pilih menu makanan Anda di atas untuk memulai konsultasi.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="disclaimer">
        <b>Scentara Premium v3.2</b><br>
        All rights reserved. Data based on perfume chemistry principles & dermatology research.<br>
        <i>Disclaimer: Hasil reaksi bisa berbeda tergantung genetika dan kondisi hormon individu.</i>
    </div>
""", unsafe_allow_html=True)
