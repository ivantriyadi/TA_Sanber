import streamlit as st
import pandas as pd

st.subheader("Proses Sentiment Analysis Dataset")
st.write('Clean tweet dalam dataset pandas')

data=pd.read_csv('assets/Clean_tweet.csv')
st.dataframe(data)

proses_names = ['Persiapkan Library','Penerjemahan','Analisis Sentimen NLTK','Visualisasi Data']
proses = st.radio('Pilih Proses', proses_names)

if proses == 'Persiapkan Library':
    st.subheader('Proses mempersiapkan library')
    st.markdown(
        """
        Pada proses ini, dilakukan instalasi library yang dibutuhkan, diantaranya Pandas untuk memproses dataset
        Deeptranslator untuk menterjemahkan kata, NLTK untuk melakukan analysis sentimen dan Matplotlib untuk
        memvisualisasikan data dalam bentuk diagram dan grafik, serta Wordcloud untuk memvisualisasikan kata yang
        sering muncul pada suatu sentimen. 
        """)
    st.image("assets/2-library.jpg")
    
elif proses == 'Penerjemahan':
    st.subheader('Proses penerjemahan kata')
    st.markdown(
        """
        Pada proses ini, dilakukan penerjemahan setiap kata dari bahasa Indonesia ke bahasa Inggris disebabkan NLTK
        belum mempunyai model analisis sentimen untuk bahasa Indonesia.
        """)
    st.image("assets/2-translating.jpg")
    
elif proses == 'Analisis Sentimen NLTK':
    st.subheader('Proses analisis sentimen')
    st.markdown(
        """
        Pada proses ini, dilakukan sentimen analisis menggunakan modul pada library NLTK yang menghasilkan Polarity Score
        negatif, netral, positif dan compound. Skor compound digunakan untuk menentukan klasifikasi sentimen apakah positif,
        netral, atau negatif.
        """)
    st.image("assets/2-analysis.jpg")
    
elif proses == 'Visualisasi Data':
    st.subheader('Proses visualisasi data')
    st.markdown(
        """
        Pada proses ini, dilakukan visualisasi data dalam bentuk pie chart dan wordcloud untuk mempermudah pengambilan
        kesimpulan.
        """)
    st.image("assets/2-visualization.jpg")
    st.image("assets/2-wordcloud.jpg")
    
else:
    st.write('proses lain')
