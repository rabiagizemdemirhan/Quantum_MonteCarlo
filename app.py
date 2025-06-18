# Potansiyel seçimi

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from metropolis import metropolis_sampling
from potential import harmonic_potential, double_well_potential, barrier_potential


pot_type = st.selectbox("Potansiyel Fonksiyonu", ["Harmonik", "Çift Kuyu", "Bariyer"])

if pot_type == "Harmonik":
    selected_potential = harmonic_potential
elif pot_type == "Çift Kuyu":
    selected_potential = double_well_potential
else:
    selected_potential = barrier_potential

# Slider ayarları

steps = st.slider("Adım Sayısı", 1000, 50000, 10000)
beta = st.slider("Beta (1/kT)", 0.1, 5.0, 1.0)

# Simülasyon

if st.button("Simülasyonu Başlat"):
    samples = metropolis_sampling(
        initial_x=0.0,
        steps=steps,
        step_size=1.0,
        beta=beta,
        potential=selected_potential  # 🔥 burada kritik düzeltme var
    )

    x_vals = np.linspace(-3, 3, 300)
    V_vals = [selected_potential(x) for x in x_vals]

    fig, ax = plt.subplots()
    ax.hist(samples, bins=100, density=True, alpha=0.6, label="Olasılık Yoğunluğu")
    ax.plot(x_vals, V_vals, 'r--', label="Potansiyel Eğrisi")  # potansiyel çizimi
    ax.set_title(f"{pot_type} Potansiyeli ile Monte Carlo Simülasyonu")
    ax.set_xlabel("Konum (x)")
    ax.set_ylabel("Yoğunluk / Enerji")
    ax.legend()
    st.pyplot(fig)
    
# İndirme Butonu
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button("📥 Grafiği İndir", buf.getvalue(), "simulasyon_grafigi.png", "image/png")