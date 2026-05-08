import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# DATA PENELITIAN
# =========================

data = {
    'Perlakuan': ['C1','C2','C3','C4','C5','E1','E2','E3','E4','E5'],
    'pH': [4.73,4.39,4.64,4.48,4.41,5.33,5.06,4.97,4.83,4.72],
    'Mikroba': [4.39,2.90,0.26,0.28,1.68,8.11,3.25,4.29,2.84,1.83],
    'Fungi': [0.43,1.07,0.43,0.24,1.87,1.69,1.50,3.47,0.77,1.33]
}

df = pd.DataFrame(data)

# =========================
# JUDUL
# =========================

st.title("🌱 Simulasi Pupuk Organik Berbasis Sludge")

st.write("""
Dashboard penelitian Shinta Tahannifia  
Departemen Ilmu Tanah dan Sumberdaya Lahan IPB
""")

# =========================
# PILIH PARAMETER
# =========================

parameter = st.selectbox(
    "Pilih Parameter",
    ['pH', 'Mikroba', 'Fungi']
)

# =========================
# GRAFIK
# =========================

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(df['Perlakuan'], df[parameter])

ax.set_xlabel("Perlakuan")
ax.set_ylabel(parameter)
ax.set_title(f"Grafik {parameter}")

st.pyplot(fig)

# =========================
# TABEL DATA
# =========================

st.subheader("Data Penelitian")

st.dataframe(df)

# =========================
# ANALISIS SEDERHANA
# =========================

nilai_tertinggi = df.loc[df[parameter].idxmax()]

st.success(
    f"Perlakuan terbaik untuk parameter {parameter}: "
    f"{nilai_tertinggi['Perlakuan']}"
)
