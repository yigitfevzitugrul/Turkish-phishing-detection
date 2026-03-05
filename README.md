# 🛡️ NLP-Based Turkish Phishing and Smishing Detection System

[![Türkçe](https://img.shields.io/badge/Dil-T%C3%BCrk%C3%A7e-red)](README.tr.md)

This project is a machine learning-based defense system that detects phishing and smishing (SMS phishing) attacks in Turkish texts by combining Cybersecurity and Natural Language Processing (NLP) disciplines.

The system analyzes the structural and semantic integrity of incoming messages and warns the user against potential cyber threats.

## 🚀 Features

* **Custom Dataset:** Instead of using ready-made English datasets, a completely original and balanced Turkish dataset of **300 rows (150 Benign, 150 Phishing)** was created from scratch, tailored to current cyber attack vectors in Turkey (Cargo, E-Government, Banking, Legal/Execution).
* **Advanced Text Preprocessing:** Texts were analyzed from a cybersecurity perspective. Malicious links frequently used by attackers were detected using Regex and converted into `<URL>` tokens to prevent the model from memorizing specific links.
* **Machine Learning (TF-IDF & Logistic Regression):** Texts were vectorized using the TF-IDF (Term Frequency-Inverse Document Frequency) method and classified with high accuracy using the Logistic Regression algorithm.
* **User-Friendly Web Interface:** The project goes beyond the terminal. It has been transformed into an interactive web UI using the `Streamlit` library, allowing anyone to easily analyze messages.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Data Science & NLP:** Pandas, Scikit-Learn, Regex (re)
* **Frontend:** Streamlit

## 💻 Installation and Usage

To run the project on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/turkish-phishing-detection-nlp.git](https://github.com/YOUR_USERNAME/turkish-phishing-detection-nlp.git)
cd turkish-phishing-detection-nlp
