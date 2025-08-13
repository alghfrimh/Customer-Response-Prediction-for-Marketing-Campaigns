# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image

def run():
    # Header
    st.write('# FIFA Player Data Analysis')
    gambar = Image.open('ref_images/dump.jpg')
    st.image(gambar)

    # Latar belakang
    st.write('## Background')
    st.markdown("""
<div style="text-align: justify;">
                
Menurut laporan <a href="https://publications.fifa.com/en/annual-report-2021/around-fifa/professional-football-2021/" target="_blank">FIFA 2022</a>, jumlah pemain sepakbola pada tahun 2021 kurang lebih sebanyak 130.000 pemain. 
Namun, dalam dataset yang digunakan pada kali ini, hanya mencakup 20.000 pemain saja.  

Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup kemungkinan untuk lahirnya talenta/wonderkid baru.  

Project ini akan dibuat menggunakan algoritma <b>Linear Regression</b> dan akan dievaluasi dengan menggunakan metrics <b>MAE (Mean Absolute Error)</b> dengan target error ±1.
                
</div>
""", unsafe_allow_html=True)
    
    # Load Dataset
    st.write('## Dataset')
    data = pd.read_csv('marketing_cmp_cleaned.csv')
    data
    # Tampilkan DataFrame
    st.dataframe(data)

    # EDA
    st.write('## Exploratory Data Analysis')
    st.write('### Player Rating Distribution')
    fig = plt.figure()
    sns.histplot(data['Overall'], kde=True, bins=30)
    plt.title('Histogram of Rating')
    st.pyplot(fig)

    # Visualisasi berdasarkan input
    pilihan = ['PaceTotal', 'ShootingTotal', 'PassingTotal',
                'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal']
    select = st.selectbox('Input field untuk visualisasi', pilihan)

    fig = plt.figure()
    sns.histplot(data[select], kde=True, bins=30)
    plt.title(f'Histogram of {select}')
    st.pyplot(fig)

    # Plotly Express
    st.write('### Tinggi vs Berat Pemain')
    chart = px.scatter(data, x='Weight', y='Height')
    st.plotly_chart(chart)

