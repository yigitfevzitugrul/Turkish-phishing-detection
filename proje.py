import pandas as pd
import re
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


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


X = df_tum['temiz_text']
y = df_tum['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Eğitim verisi boyutu:", X_train.shape)
print("Test verisi boyutu:", X_test.shape)
print("\nÖrnek eğitim verileri:")
print(X_train.head(3).values)


vectorizer = TfidfVectorizer()
X_train_vektor = vectorizer.fit_transform(X_train)
X_test_vektor = vectorizer.transform(X_test)


model = LogisticRegression(random_state=42)
model.fit(X_train_vektor, y_train)


y_tahmin = model.predict(X_test_vektor)

print("-" * 40)
print("🚀 Model Başarı Oranı (Accuracy):", accuracy_score(y_test, y_tahmin))
print("\n📊 Detaylı Sınıflandırma Raporu:\n", classification_report(y_test, y_tahmin))


ornek_mesaj = ["Kargonuz adresinize teslim edilememistir. Tekrar gonderim icin adresinizi guncelleyin: http://ptt-kargo-guncelle.com"]

ornek_temiz = [metin_temizle(ornek_mesaj[0])]
ornek_vektor = vectorizer.transform(ornek_temiz)

tahmin = model.predict(ornek_vektor)

print("-" * 40)
if tahmin[0] == 1:
    print(f"🚨 TEST SONUCU: Yazdığınız mesaj ZARARLI (Oltalama) olarak algılandı!")
else:
    print(f"✅ TEST SONUCU: Yazdığınız mesaj TEMİZ olarak algılandı.")