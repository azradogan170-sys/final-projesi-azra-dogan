import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


st.set_page_config(page_title="SUV Fiyat Tahmin Sistemi", layout="centered")
st.title("🚗 SUV Araç Fiyat Tahmin Yapay Zekası")
st.write("Aracın özelliklerini seçerek yapay zekanın pazar tahmin fiyatını görebilirsiniz.")


mevcut_klasor = os.path.dirname(__file__) if '__file__' in locals() else os.getcwd()

@st.cache_resource
def modeli_yukle():
    model_yolu = os.path.join(mevcut_klasor, 'suv_fiyat_modeli.pkl')
    sutun_yolu = os.path.join(mevcut_klasor, 'model_sutunlari.pkl')
    
    model = joblib.load(model_yolu)
    sutunlar = joblib.load(sutun_yolu)
    return model, sutunlar

try:
    yapay_zeka, model_sutunlari = modeli_yukle()
    model_yuklendi = True
except Exception as e:
    model_yuklendi = False
    st.error(f"Model dosyaları bulunamadı! Lütfen pkl dosyalarının depoda olduğundan emin olun. Hata detayı: {e}")


st.subheader("📋 Araç Bilgilerini Giriniz")

marka = st.selectbox("Araç Markası Seçin:", ["Chery", "Nissan", "Hyundai", "Dacia", "Kia"])
yil = st.number_input("Araç Yılı (Model):", min_value=2010, max_value=2026, value=2022, step=1)
kilometre = st.number_input("Aracın Kilometresi:", min_value=0, max_value=500000, value=50000, step=1000)
talep_skoru = st.slider("Aracın Pazardaki Talep Skoru (1: Düşük, 5: Çok Popüler):", 1, 5, 3)


if st.button("💰 Fiyat Tahmini Yap", type="primary"):
    if not model_yuklendi:
        st.error("Yapay zekâ modeli yüklenemediği için şu an tahmin yapılamıyor.")
    else:
        girdi_verisi = pd.DataFrame([[marka, yil, kilometre, talep_skoru]], 
                                    columns=['Marka', 'Yil', 'Kilometre', 'Talep_Skoru'])
        
        girdi_encoded = pd.get_dummies(girdi_verisi)
        
        for col in model_sutunlari:
            if col not in girdi_encoded.columns:
                girdi_encoded[col] = 0
                
        girdi_encoded = girdi_encoded[model_sutunlari]
        
        tahmin_edilen_fiyat = yapay_zeka.predict(girdi_encoded)[0]
        
        st.success(f"### 🎯 Yapay Zekâ Pazar Tahmini: {tahmin_edilen_fiyat:,.2f} TL")
        st.caption("Not: Bu fiyat regresyon modelinin %72.20 başarı oranıyla pazar verilerinden öğrendiği tahmini değerdir.")
