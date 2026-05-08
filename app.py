import streamlit as st
st.markdown("""
<style>

/* Tombol collapse sidebar */
button[kind="header"] {
    background-color: #2E8B57;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 6px 10px;
}

/* Hover effect */
button[kind="header"]:hover {
    background-color: #3CB371;
    color: white;
}

</style>
""", unsafe_allow_html=True)
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# DATA DASAR PENELITIAN
# =====================================

data = {
    'Perlakuan': ['C1','C2','C3','C4','C5','E1','E2','E3','E4','E5'],
    'pH': [4.73,4.39,4.64,4.48,4.41,5.33,5.06,4.97,4.83,4.72],
    'Mikroba': [4.39,2.90,0.26,0.28,1.68,8.11,3.25,4.29,2.84,1.83],
    'Fungi': [0.43,1.07,0.43,0.24,1.87,1.69,1.50,3.47,0.77,1.33]
}

df = pd.DataFrame(data)

# =====================================
# HEADER
# =====================================

col1, col2 = st.columns([1,5])

with col1:
    st.image("logo_IPB.png", width=90)

with col2:
    st.title("🌱 Soil Sludge Simulation")
    st.subheader("Simulasi Formulasi Pupuk Organik Berbasis Sludge")

st.write("""
Aplikasi simulasi penelitian:
Shinta Tahannifia
Departemen Ilmu Tanah dan Sumberdaya Lahan IPB
""")

# =====================================
# SIDEBAR INPUT
# =====================================

st.sidebar.header("🌱 Soil Control Panel")

jenis = st.sidebar.selectbox(
    "Pilih Chelating Agent",
    ["Citric Acid", "EDTA"]
)

konsentrasi = st.sidebar.slider(
    "Konsentrasi (%)",
    0,
    125,
    50
)

# =====================================
# MODEL SIMULASI SEDERHANA
# =====================================

if jenis == "EDTA":
    simulasi_pH = 5.3 - (konsentrasi * 0.005)
    simulasi_mikroba = 8 - (konsentrasi * 0.04)
    simulasi_fungi = 1 + (konsentrasi * 0.02)

else:
    simulasi_pH = 4.8 - (konsentrasi * 0.003)
    simulasi_mikroba = 4 - (konsentrasi * 0.03)
    simulasi_fungi = 0.5 + (konsentrasi * 0.01)

# =====================================
# HASIL SIMULASI
# =====================================

st.header("📊 Hasil Simulasi")

col1, col2, col3 = st.columns(3)

col1.metric("pH Tanah", round(simulasi_pH, 2))
col2.metric("Total Mikroba", round(simulasi_mikroba, 2))
col3.metric("Total Fungi", round(simulasi_fungi, 2))

# =====================================
# VISUALISASI
# =====================================

sim_data = pd.DataFrame({
    'Parameter': ['pH', 'Mikroba', 'Fungi'],
    'Nilai': [
        simulasi_pH,
        simulasi_mikroba,
        simulasi_fungi
    ]
})

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(sim_data['Parameter'], sim_data['Nilai'])

ax.set_title("Visualisasi Hasil Simulasi")

st.pyplot(fig)

# =====================================
# INTERPRETASI
# =====================================

st.header("🧪 Interpretasi")

if simulasi_pH < 4.5:
    st.warning("Tanah sangat masam")

elif simulasi_pH < 5.5:
    st.info("Tanah masam")

else:
    st.success("pH tanah relatif baik")

if simulasi_mikroba > 5:
    st.success("Aktivitas mikroba tinggi")

else:
    st.warning("Aktivitas mikroba rendah")

# =====================================
# DATA ASLI PENELITIAN
# =====================================

st.header("📁 Data Asli Penelitian")

st.dataframe(df)
