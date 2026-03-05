import streamlit as st
import pandas as pd
import re
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


st.set_page_config(page_title="Siber Güvenlik | NLP Oltalama Tespiti", page_icon="🛡️")

@st.cache_resource
def modeli_hazirla():
    
    df_zararli = pd.read_csv("veri setlerim/zararli.csv")
    df_temiz = pd.read_csv("veri setlerim/temiz.csv")
    
    df_zararli['label'] = 1
    df_temiz['label'] = 0
    
    df_tum = pd.concat([df_zararli, df_temiz], ignore_index=True)
    df_tum = shuffle(df_tum, random_state=42).reset_index(drop=True)
    
    
    def metin_temizle(text):
        text = str(text).lower()
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' <URL> ', text)
        text = re.sub(r'www\.\S+', ' <URL> ', text)
        text = re.sub(r'[^\w\s<>]', '', text) 
        return text

    df_tum['temiz_text'] = df_tum['text'].apply(metin_temizle)
    
    
    vectorizer = TfidfVectorizer()
    X_vektor = vectorizer.fit_transform(df_tum['temiz_text'])
    y = df_tum['label']
    
    model = LogisticRegression(random_state=42)
    model.fit(X_vektor, y)
    
    return model, vectorizer, metin_temizle


model, vectorizer, metin_temizle = modeli_hazirla()



st.title("🛡️ NLP Tabanlı Oltalama (Phishing) Tespiti")
st.write("Bu uygulama, yapay zeka kullanarak şüpheli SMS veya e-posta metinlerini analiz eder. Mesajın bir siber tehdit olup olmadığını tespit edebilirsiniz.")


mesaj = st.text_area("Analiz edilecek mesajı buraya yapıştırın:", height=150, placeholder="Örn: Kargonuz teslim edilemedi, hemen tıklayın...")


if st.button("🔍 Mesajı Analiz Et"):
    if mesaj.strip() == "":
        st.warning("Lütfen analiz etmek için bir metin girin.")
    else:
        
        temiz_mesaj = metin_temizle(mesaj)
        vektor = vectorizer.transform([temiz_mesaj])
        
        tahmin = model.predict(vektor)[0]
        olasilik = model.predict_proba(vektor)[0] 
        
        st.markdown("---")
        if tahmin == 1:
            guven_orani = olasilik[1] * 100
            st.error(f"🚨 DİKKAT! Bu mesaj bir OLTALAMA (Phishing/Smishing) saldırısı olabilir!")
            st.write(f"**Yapay Zekanın Tehdit İhtimali Tahmini:** %{guven_orani:.2f}")
        else:
            guven_orani = olasilik[0] * 100
            st.success(f"✅ GÜVENLİ! Bu mesaj temiz görünüyor.")
            st.write(f"**Yapay Zekanın Güvenilirlik İhtimali Tahmini:** %{guven_orani:.2f}")