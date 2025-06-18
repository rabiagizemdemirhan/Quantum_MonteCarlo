# 🧠 Kuantum Monte Carlo Simülatörü

Bu proje, harmonik, çift kuyu ve bariyer potansiyelleri altında kuantum parçacıkların konum dağılımlarını simüle etmek için Monte Carlo yöntemini (Metropolis algoritması) kullanır.  
Ayrıca Streamlit ile görselleştirilmiş, etkileşimli bir arayüz sunar. 👩‍💻✨

---

## 📸 Arayüz Görünümü

Simülasyon sonucu histogram (olasılık yoğunluğu) ve potansiyel eğrisi birlikte gösterilir:

![Simülasyon Arayüzü](docs/Ekran%20Resmi%202025-06-18%2018.57.44.png)

---

## 🚀 Özellikler

- 🎛 Potansiyel fonksiyonu seçimi: Harmonik, Çift Kuyu, Bariyer
- 📊 Histogram + potansiyel eğrisi birlikte çizimi
- ⚙️ Etkileşimli kontrol: adım sayısı ve sıcaklık (β)
- 📥 Simülasyon grafiğini PNG olarak indirme
- 🌐 Streamlit tabanlı kullanıcı arayüzü

---

## 🛠 Kullanılan Teknolojiler

- Python 3
- NumPy
- Matplotlib
- Streamlit

---

## 🔬 Kullanılan Yöntem: Metropolis Algoritması

Monte Carlo simülasyonlarında yaygın olarak kullanılan **Metropolis algoritması**, önerilen yeni konumların potansiyele göre kabul edilip edilmeyeceğine karar verir.  
Bu sayede zaman içinde olasılık yoğunluğu dağılımı örneklenmiş olur.

---

## ⚙️ Kurulum ve Kullanım

### 1. Gerekli kütüphaneleri yükle:

```bash
pip install streamlit numpy matplotlib
```

### 2. Uygulamayı başlat:

```bash
streamlit run app.py
```

---

## 📁 Dosya Yapısı

```
Quantum_MonteCarlo/
├── app.py                ← Streamlit arayüzü
├── metropolis.py         ← Metropolis örnekleme algoritması
├── potential.py          ← Potansiyel fonksiyonları
├── README.md             ← Bu dosya
└── docs/
    └── screenshot.png    ← Ekran görüntüsü
```

---

## 👩‍💻 Geliştirici

**Gizem Demirhan**  
🎓 Fizik & Bilgisayar Programlama  
🚀 Monte Carlo'dan kuantuma, Streamlit'ten görselliğe

---

## 📜 Lisans

MIT License © 2025 Gizem D.
