# 🛡️ NLP Tabanlı Türkçe Oltalama (Phishing) ve Smishing Tespit Sistemi

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Bu proje, Siber Güvenlik ve Doğal Dil İşleme (NLP) disiplinlerini bir araya getirerek, Türkçe metinlerdeki oltalama (phishing) ve sahte SMS (smishing) saldırılarını tespit eden makine öğrenmesi tabanlı bir savunma sistemidir. Gelen mesajların yapısal ve anlamsal bütünlüğünü analiz ederek olası siber tehditleri gerçek zamanlı olarak sınıflandırır.

---

## 📊 Veri Seti ve Model Performansı

Model, internetteki hazır ve hatalı çeviri veri setleri yerine, Türkiye'deki güncel siber saldırı vektörlerine özel olarak sıfırdan oluşturulmuş özgün bir veri seti ile eğitilmiştir.

### Veri Seti Dağılımı
| Kategori | Temiz (Benign) Veri Sayısı | Zararlı (Phishing) Veri Sayısı | Toplam |
| :--- | :---: | :---: | :---: |
| **Kargo & Lojistik** | 30 | 30 | 60 |
| **Banka & Ekonomi** | 30 | 30 | 60 |
| **Hukuk & İcra (UYAP vb.)** | 10 | 30 | 40 |
| **Teknoloji & Sosyal Medya** | 50 | 40 | 90 |
| **Kamu & Kurum (E-Devlet vb.)**| 30 | 20 | 50 |
| **TOPLAM** | **150** | **150** | **300** |

### Lojistik Regresyon Test Metrikleri
Test verisi (%20 oranında ayrılmış) üzerinde yapılan sınıflandırma raporu sonuçları:

| Sınıf | Precision (Kesinlik) | Recall (Duyarlılık) | F1-Score |
| :--- | :---: | :---: | :---: |
| **0 (Temiz)** | 1.00 | 1.00 | 1.00 |
| **1 (Zararlı)** | 1.00 | 1.00 | 1.00 |
| **Genel Doğruluk (Accuracy)** | **-** | **-** | **%100.0** |

*(Not: Veri seti genişletildikçe modelin gerçek hayat senaryolarındaki başarı oranlarının daha objektif seviyelere stabilize olması hedeflenmektedir.)*

---

## ⚙️ Mimari ve Teknik Altyapı

1. **Gelişmiş Metin Ön İşleme:** Saldırganların sık kullandığı zararlı bağlantılar Regex ile yakalanır ve `<URL>` token'larına dönüştürülür. Bu, modelin belirli domainleri ezberlemesini (overfitting) engeller.
2. **Vektörizasyon (TF-IDF):** Metinler, seyrek (sparse) matrislere dönüştürülerek kelimelerin doküman içindeki ayırt edicilik ağırlıkları hesaplanır.
3. **Sınıflandırma:** Vektörize edilen veriler, hiperparametreleri optimize edilmiş Lojistik Regresyon modeli ile sınıflandırılır ve sonuçlar olasılık yüzdesi ile kullanıcıya sunulur.

---

## 💻 Geliştiriciler İçin Kurulum Rehberi

Projeyi kendi lokal ortamınızda çalıştırmak ve test etmek için aşağıdaki adımları sırasıyla izleyin. Kütüphane çakışmalarını önlemek adına **sanal ortam (virtual environment)** kullanılması şiddetle tavsiye edilir.

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/yigitfevzitugrul/Turkish-phishing-detection.git](https://github.com/yigitfevzitugrul/Turkish-phishing-detection.git)
cd Turkish-phishing-detection





