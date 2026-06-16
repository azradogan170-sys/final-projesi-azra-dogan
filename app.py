import streamlit as pd
import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(page_title="SUV Fiyat Tahmin Sistemi", layout="centered")
st.title("🚗 SUV Araç Fiyat Tahmin Yapay Zekası")
st.write("Aracın özelliklerini seçerek yapay zekanın pazar tahmin fiyatını görebilirsiniz.")


@st.cache_resource
def modeli_yukle():
    model = joblib.load('suv_fiyat_modeli.pkl')
    sutunlar = joblib.load('model_sutunlari.pkl')
    return model, sutunlar

try:
    yapay_zeka, model_sutunlari = modeli_yukle()
except:
    st.error("Model dosyaları bulunamadı! Lütfen pkl dosyalarının app.py ile aynı klasörde olduğundan emin olun.")


st.subheader("📋 Araç Bilgilerini Giriniz")


marka = st.selectbox("Araç Markası Seçin:", ["Chery", "Nissan", "Hyundai", "Dacia", "Kia"])


yil = st.number_input("Araç Yılı (Model):", min_value=2010, max_value=2026, value=2022, step=1)
kilometre = st.number_input("Aracın Kilometresi:", min_value=0, max_value=500000, value=50000, step=1000)


talep_skoru = st.slider("Aracın Pazardaki Talep Skoru (1: Düşük, 5: Çok Popüler):", 1, 5, 3)


if st.button("💰 Fiyat Tahmini Yap", type="primary"):
    
   
    girdi_verisi = pd.DataFrame([[marka, yil, kilometre, talep_skoru]], 
                                columns=['Marka', 'Yil', 'Kilometre', 'Talep_Skoru'])
    
    
    girdi_encoded = pd.get_dummies(girdi_verisi)
    
    
    for col in model_sutunlari:
        if col not in girdi_encoded.columns:
            girdi_encoded[col] = 0
            
    
    girdi_encoded = girdi_encoded[model_sutunlari]
    
    
    tahmin_edilen_fiyat = yapay_zeka.predict(girdi_encoded)[0]
    
    # Sonucu ekrana çok şık bir şekilde yazdırıyoruz
    st.success(f"### 🎯 Yapay Zekâ Pazar Tahmini: {tahmin_edilen_fiyat:,.2f} TL")
    st.caption("Not: Bu fiyat regresyon modelinin %72.20 başarı oranıyla pazar verilerinden öğrendiği tahmini değerdir.")
